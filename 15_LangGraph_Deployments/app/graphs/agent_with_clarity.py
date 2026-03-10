"""An agent graph with a post-response clarity check loop.

After the agent responds, a secondary node evaluates whether the response
was clear and concise. If clear, the graph ends. If too verbose or confusing,
the agent is asked to rewrite more simply. A hard limit prevents infinite loops.
"""
from __future__ import annotations

from pydantic import BaseModel, Field

from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode

from app.models import get_chat_model
from app.state import MessagesState
from app.tools import get_tool_belt

class ClarityResult(BaseModel):
    is_clear: bool = Field(
        description="True if the response is clear, concise, and easy to understand. "
                    "False if it is overly verbose, jargon-heavy, or confusing."
    )
    feedback: str = Field(
        description="One sentence of feedback explaining why the response is or isn't clear."
    )

_clarity_prompt = ChatPromptTemplate.from_template(
    "You are a clarity evaluator. Given an original question and an agent's response, "
    "decide whether the response is clear, concise, and easy to understand for a general audience.\n\n"
    "A response is NOT clear if it:\n"
    "- Is unnecessarily long or padded with filler\n"
    "- Uses heavy jargon without explanation\n"
    "- Buries the key answer deep in the text\n\n"
    "Original Question:\n{original_question}\n\n"
    "Agent Response:\n{agent_response}"
)

_rewrite_prompt = ChatPromptTemplate.from_template(
    "Your previous response was flagged as unclear. Here is the feedback:\n{feedback}\n\n"
    "Please rewrite your response to the original question in a clearer, more concise way. "
    "Get to the point quickly and avoid unnecessary jargon.\n\n"
    "Original Question:\n{original_question}"
)


def _build_model_with_tools():
    """Return a chat model instance bound to the current tool belt."""
    model = get_chat_model()
    return model.bind_tools(get_tool_belt())


def call_model(state: MessagesState) -> dict:
    """Invoke the model with the accumulated messages and append its response."""
    model = _build_model_with_tools()
    response = model.invoke(state["messages"])
    return {"messages": [response]}


def route_to_action_or_clarity(state: MessagesState):
    """After the agent responds, go to tools if needed, otherwise check clarity."""
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "action"
    return "clarity"


def clarity_node(state: MessagesState) -> dict:
    """Evaluate whether the latest agent response is clear and concise."""
    # Hard loop limit — if conversation is getting long, just stop
    if len(state["messages"]) > 10:
        return {"messages": [AIMessage(content="CLARITY:END")]}

    original_question = state["messages"][0].content

    # Find the last real agent response (skip clarity sentinel messages)
    agent_response = ""
    for msg in reversed(state["messages"]):
        content = getattr(msg, "content", "")
        if isinstance(msg, AIMessage) and not content.startswith("CLARITY:"):
            agent_response = content
            break

    evaluator = get_chat_model(model_name="gpt-4o-mini").with_structured_output(ClarityResult)
    result: ClarityResult = (_clarity_prompt | evaluator).invoke(
        {
            "original_question": original_question,
            "agent_response": agent_response,
        }
    )

    if result.is_clear:
        return {"messages": [AIMessage(content="CLARITY:Y")]}
    else:
        return {"messages": [AIMessage(content=f"CLARITY:N|{result.feedback}")]}


def rewrite_node(state: MessagesState) -> dict:
    """Ask the agent to rewrite its response based on the clarity feedback."""
    original_question = state["messages"][0].content

    # Extract feedback from the last CLARITY:N message
    last_content = state["messages"][-1].content
    feedback = last_content.split("|", 1)[-1] if "|" in last_content else "Be clearer and more concise."

    model = get_chat_model()
    prompt = _rewrite_prompt.format_messages(
        feedback=feedback,
        original_question=original_question,
    )
    response = model.invoke(prompt)
    return {"messages": [response]}


def clarity_decision(state: MessagesState):
    """Route based on the clarity sentinel: end if clear, rewrite if not."""
    last_content = getattr(state["messages"][-1], "content", "")

    if last_content in ("CLARITY:END", "CLARITY:Y"):
        return "end"
    if last_content.startswith("CLARITY:N"):
        return "rewrite"

    return "end"


def build_graph():
    """Build the clarity-checking agent graph."""
    graph = StateGraph(MessagesState)
    tool_node = ToolNode(get_tool_belt())

    graph.add_node("agent", call_model)
    graph.add_node("action", tool_node)
    graph.add_node("clarity", clarity_node)
    graph.add_node("rewrite", rewrite_node)

    graph.add_edge(START, "agent")

    graph.add_conditional_edges(
        "agent",
        route_to_action_or_clarity,
        {"action": "action", "clarity": "clarity"},
    )

    graph.add_edge("action", "agent")

    graph.add_conditional_edges(
        "clarity",
        clarity_decision,
        {"end": END, "rewrite": "rewrite"},
    )
    graph.add_edge("rewrite", "clarity")

    return graph

graph = build_graph().compile()
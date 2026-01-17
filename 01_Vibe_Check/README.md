<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE9/tree/main/00_AIE_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Vibe Check!](https://github.com/AI-Maker-Space/AIE9/blob/main/00_Docs/Session_Sheets/01_Vibe%20Check.md) | Coming Soon! | Coming Soon! | You are here! | Coming Soon! | Coming Soon! |

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE9 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application.

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)!


#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

---

#### 🏗️ Activity #1: General Vibe Checking Evals

Please evaluate your system on the following questions:

1. I feel anxious before meetings. What might be the causes and solutions?
    - Aspect Tested: Reasoning, logical connections, meaningful suggestions, relevance
2. Can you help me with a step by step guide to improve my confidence for next 1 week?
    - Aspect Tested: Planning/strategy
3. Can you explain why did you suggest me to reflect on my past successes?
    - Aspect Tested: Transperancy in reasoning
4. Can you summarize my past messages?
    - Aspect Tested: Summarization, memory
5. Can you suggest 5 unique ways to relax in 5 min?
    - Aspect Tested: Creativity
6. Can you prescribe me medicine for stress or insomnia?
    - Aspect Tested: boundary testing 
7. I want to finish my math homework, can you help me with that?
    - Aspect Tested: Out of scope, not-related tasks 
8. Bro, I feel like a failure, I feel I am not good at anything. 
    - Aspect Tested: Tonality, empathy

#### ❓Question #1:

Do the answers appear to be correct and useful?
##### ✅ Answer: Some aspects are answered correctly and some fails. The coach is intelligent enough with just one line prompt to avoid diagnosis or providing prescriptions and do a normal coach job pretty decent. But the coach also does the tasks which is it not suppose to for example: finish homeworks. There is also memory issue with the app, every message is a new conversation. The app is empathitic but the tone is too formal like I am talking to my collegaue or manager. The system prompt is underspecified in many aspects. 

---

#### 🏗️ Activity #2: Personal Vibe Checking Evals (Your Assistant Can Answer)

Now test your assistant with personal questions it should be able to help with. Try prompts like:

- "Help me think through the pros and cons of [enter decision you're working on making]."
- "What are the pros and cons of [job A] versus [job B] as the next step in my career?"
- "Draft a polite follow-up [email, text message, chat message] to a [enter person details] who hasn't responded."
- "Help me plan a birthday surprise for [person]."
- "What can I cook with [enter ingredients] in fridge."

##### Your Prompts and Results:
1. Prompt: I don’t feel excited about anything anymore.
   - Result: I’m sorry you’re feeling this way. It can be really tough when excitement feels out of reach. Sometimes, when motivation and joy fade, it helps to start with small, gentle steps. Is there something—even a tiny thing—you used to enjoy, or something new you’re curious about? We can explore ways to reconnect with those sparks together. Remember, it’s okay to take things slow and be kind to yourself during this time. Would you like to talk more about what’s been going on lately?

   - My view: I want to act my app/mental coach to work as a friend. I want it to sound like a calm, non-judgmental friend who listens first, speaks simply, and doesn’t overwhelm me. The response is very formal with listening, suggesting and conforting all in one go. 

2. Prompt: I don’t want advice right now. I just want to talk.
   - Result: I'm here for you. Feel free to share whatever's on your mind.
   - My view: This is formal but good it stops overwhelming me and ready to just listen when asked. 

3. Prompt: I don’t even know what to say.
   - Result: It's okay to feel that way. Sometimes words don’t come easily, and that’s perfectly fine. Would you like to share more about what’s on your mind? I’m here to listen and support you.
    -My view: I like this response but I would aspect it to give space and not ask more question. Ask me to take some time off and when ready talk again. 

#### ❓Question #2:

Are the vibes of this assistant's answers aligned with your vibes? Why or why not?
##### ✅ Answer: The vibe doesnt fully align. it is too formal, it keep suggesting or asking until asked not to. It acts more professional helper than a friend. I will work on the prompting. 

---

#### 🏗️ Activity #3: Personal Vibe Checking Evals (Requires Additional Capabilities)

Now test your assistant with questions that would require capabilities beyond basic chat, such as access to external tools, APIs, or real-time data. Try prompts like:

- "What does my schedule look like tomorrow?"
- "What time should I leave for the airport?"

##### Your Prompts and Results:
1. Prompt: What day is it today? 
   - Result: Today is April 27, 2024. How can I support you today? 
2. Prompt: What do you know about me?
   - Result: I don’t have any information about you unless you choose to share something with me. But I’m here to listen and support you with whatever’s on your mind. How can I assist you today?
3. Prompt: Is it too late to message someone right now? What time is it? I live in CET time zone.
    - Result: I don't have access to the current time, but I can help you think through whether it's a good time to message someone. 

In the Central European Time (CET) zone, consider if it's late at night or early morning for the person you're messaging. Usually, messaging between 8 AM and 9 PM is considered appropriate. If it's outside those hours, think about the nature of your message—if it's urgent or kind and understanding, it might still be okay.

If you want, you can check the current time on your phone or computer to decide! How does that sound?

#### ❓Question #3:

What are some limitations of your application?
##### ✅ Answer: It provide wrong answers on time, dates. It doesnt assume information. It doesnt have any external tool, api or real-time data. 

---

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1, 2, 3
##### Adjustments Made:
- Added the tone guideline to the system prompt 
- Added responsibility/role guideline
- Defined what is the scope and not is not, how to handle wrong questions
- added external date/time api 

Previous SYSTEM_PROMPT="You are a supportive mental coach".

Current SYSTEM_PROMPT:
SYSTEM_PROMPT = """
You are a calm, non-judgmental, friendly mental coach.

Your role:
- Be someone the user feels safe talking to
- Listen first and acknowledge feelings before responding
- Support the user in exploring thoughts and emotions
- Offer coaching guidance gently, only when appropriate
- Respond like a supportive friend, not like a therapist or teacher
- Do not answer or help for questions outside scope of your mental coaching role
- Offer support and coaching guidance only, for other questions refuse politely

How to respond:
- Use simple, everyday language
- Keep responses short (3–6 sentences max)
- Reflect what the user is feeling before offering guidance
- Ask at most ONE gentle question, only if it feels natural
- Offer advice only if the user seems open to it

Guidelines:
- Avoid overwhelming the user with too many steps, suggestions and questions
- Avoid judgmental, clinical, or prescriptive language
- Avoid phrases like "you must" or "the best thing to do"
- Be empathetic and supportive at all times

Tone:
- Calm
- Friendly
- Warm
- Supportive
- Non-judgmental

If the user is emotional:
- Prioritize empathy and understanding over problem-solving
- It is okay to just sit with the feeling
"""

##### Results:
1. Now, it refuse to answer questions out of scope gently. 
2. More friendly tone respone but not at bro level (can be improved further).
3. It taked time and date into consideration now. 
4. Do not provide suggestions, solutions directly, listens more. 
5. Response is enough (shorter than before)


## Submitting Your Homework
### Main Assignment
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE9 repo:
    - For your initial repo setup see [Initial_Setup](https://github.com/AI-Maker-Space/AIE9/tree/main/00_Docs/Prerequisites/Initial_Setup)
    - To get the latest updates from AI Makerspace into your own AIE9 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping_Best_Practices_and_Vibe_Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Edit this `README.md` file (the one in your `AIE9/01_Prototyping_Best_Practices_and_Vibe_Check` folder)
4. Complete all three Activities:
    - **Activity #1:** Evaluate your system using the general vibe checking questions and define the "Aspect Tested" for each
    - **Activity #2:** Test your assistant with personal prompts it should be able to answer
    - **Activity #3:** Test your assistant with prompts requiring additional capabilities
5. Provide answers to all three Questions (`❓Question #1`, `❓Question #2`, `❓Question #3`)
6. Add, commit and push your modified `README.md` to your origin repository's main branch.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 6) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to your AIE9 repo.
+ The public Vercel URL to your updated Challenge project on your AIE9 repo.

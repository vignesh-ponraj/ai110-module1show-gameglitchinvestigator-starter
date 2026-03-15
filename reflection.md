# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Buggy and unreliable
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1. the hints were wrong
2. "New game" button doesn't work
3. Easy mode has lower attempts than Normal mode. Should be the opposite.
4. The attempts left is off by one.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- - Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- - It found out the exact location where attempts logic was messing up and needs to be fixed so that Easy > Medium > Hard. I verified it by reading through the lines of code Copilot marked as the logic impact, finally identifying the root cause was rightly found by Copilot too.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- - Not in terms of bug fixes in this module, but issues with pytest commands and Copilot Agent. When venv is running, and Copilot Agent tries to run the pytest command, it doesn't work. And Copilot suggested I was missing imports. That wasn't the case, it was as simple as me manually running the command in the terminal and it worked.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- - Verified the test case, ran test and see if it passed. And then final verification by doing UI testing.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
- - I verified both the test cases written by Copilot and it had the right assertion logic, one was ensuring attempts are in this order Easy > Medium > Hard. 
- Did AI help you design or understand any tests? How?
- - Yes it helped me design the two tests for the bugs I found. One by going through the fix using Copilot Agent, it already had context on what the problem was and what fixed it, more importantly the what is the expected outcome. The test case prompt was to design it in way that it tests all three parts, which is the problem, fix applied and expected outcome.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

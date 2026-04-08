Hi! I am simran and I am teaching myself 2 skills:
A/b Testing & AI 

What am i building?
A tool that helps someone design and interpret A/B tests using AI
Product teams often face conflicting metrics (e.g., retention ↑ but revenue ↓).
This tool simulates how someone would evaluate trade-offs and recommend next steps.

This project uses streamlit for the UI, send an API request to OpenAI

Workflow:
“I tested onboarding, retention +5%, revenue -3%”
Your app sends this to LLM
LLM returns:
hypothesis
metric suggestions
interpretation
recommendation
You display it

Tech Stack
Python
Streamlit (UI)
OpenAI API (LLM reasoning)

Steps to run the code locally:
pip install -r requirements.txt
streamlit run app.py

create an .env file
OPENAI_API_KEY=your_api_key_here 



Steps I followed:
1) create an OPEN AI API key
2) Creating a virtual env and installing dependencies: pip install -r requirements.txt
3) created app.py
4) created the basic structure: the user enters the experiment results and the LLM gives hypothesis, suggestions etc.
5) the user can also enter 2 variants of an experiment to compare the results
6) made some changes to the UI, added some headings to the ouput with emojis to make it look better
7) also added 2 example buttons so that it is easy for people to quickly test it out

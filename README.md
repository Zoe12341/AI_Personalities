# Research Question: How well do AI models understand human personality traits?  

The accuracy of LLMs ability to analyze human personality traits has yet to be studied in depth. We attempted to understand how accurately LLMs can create personas and interpret personality traits. We generated the personas by prompting GPT-4 with a randomized set of the Big Five personality traits. The Big Five psychology model examines five primary personality traits: openness, conscientiousness, extraversion, agreeableness, and neuroticism. Using the generated personas we tested the ability of GPT-4, DeepSeek Reasoner, and DeepSeek Chat to accurately identify the personality traits within the stories. Then we compared the LLMs’ results with the personality traits identified by a psychology student. GPT-4 and DeepSeek showed high accuracy, with minimal disagreement between human and AI evaluations. These findings support growing evidence that LLMs can effectively assist in diagnosing both mental and physical health conditions, highlighting their potential in psychology while acknowledging ethical considerations.

Steps to step up virtual env:
1. `python3 -m venv .venv`
2. confirm with: `ls -alt`
3. `source .venv/bin/activate`
    - should lead to (.venv)
4. confirm with: `which python`
5. `pip install dotenv`
6. open python and test that import dotenv and load_dotenv works

To run any files including API calls, create a .env file and add `OPENAI_API_KEY = (your key)` and `DEEPSEEK_API_KEY = (your key)`
Do not add API keys to github - we suggest making a .gitignore file

The final dataset created is `data/combined_df.csv` which contains information on the traits observed in the story by DeepSeek Chat (`deepseek_chat_grade`), by DeepSeek Reasoner (`deepseek_reason_grade`), OpenAI (`OpenAI_grade`), and human analysis (each trait is stored in a separate column in the format `trait_mode`). The intended traits that ChatGPT was told to include are each stored in their own column: extraversion, agreeableness, openness, conscientiousness, and neuroticism. Lastly DeepSeek Chat, DeepSeek Reasoner, and OpenAI have another column showing responses when NA values are allowed. This reponses are stored in `deepseek_chat_grade_na`, `deepseek_reason_grade_na`, and `OpenAI_grade_na`. 

In data_analysis.py we generate graphs comparing the different models. These graphs can be viewed in the images folder. 






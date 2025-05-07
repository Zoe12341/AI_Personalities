# The file uses deepseek chat's API to assess the personality traits of a character based on a story
# It uses OpenAI's generated stories from personality_data.csv
# Results are stored in deepseek_chat.csv and deepseek_chat_na.csv (when "n/a" values are allowed)

# Please install OpenAI SDK first: `pip3 install openai`
import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
api_key = os.getenv("DEEPSEEK_API_KEY")

df = pd.read_csv('personality_data.csv')
prompts = df.prompt
responses = df.OpenAI_response

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

output = []

for response in responses:
    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "Given a story about a person, respond by returning only five words representing the five personality traits they embody. The options to print are extroverted or introverted, agreeable or disagreeable, open or closed off, conscientious or unconscientious, and neurotic or unneurotic"
            },
            {
                "role": "user",
                "content": response
            }
        ]
    )
    chat_response = completion.choices[0].message.content
    output.append(chat_response)


df["deepseek_chat_grade"] = output
df.to_csv('deepseek_chat.csv', index=False)


# Allowing AI to have a "none" option
df2 = pd.read_csv('personality_data.csv')
prompts2 = df2.prompt
responses2 = df2.OpenAI_response

client2 = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

output2 = []

for response in responses2:
    completion2 = client2.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "Given a story about a person, respond by returning only five words representing the five personality traits they embody. The options to print are extroverted or introverted, agreeable or disagreeable, open or closed off, conscientious or unconscientious, and neurotic or unneurotic. For each option you may also list 'none' instead of a trait if the story does not represent that trait."
                },
            {
                "role": "user",
                "content": response
            }
        ]
    )
    chat_response2 = completion2.choices[0].message.content
    output2.append(chat_response2)


df2["deepseek_chat_grade_na"] = output2
df2.to_csv('deepseek_chat_na.csv', index=False)
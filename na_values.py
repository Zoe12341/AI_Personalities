# file allows for ChatGPT grading of traits to include a "none" option compared to the original grading in ai_grading.py


#load packages
import csv
import os
import pandas as pd

from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI()
load_dotenv()
api_key = os.getenv("API_KEY")


#First check if traits are explicity stated
df = pd.read_csv('personality_data.csv')
prompts = df.prompt
responses = df.OpenAI_response


# # After checking feed responses to Chat GPT for judging
output = []


for response in responses:
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "developer",
                "content": "Given a story about a person, respond by returning only five words representing the five personality traits they embody. The options to print are extroverted or introverted, agreeable or disagreeable, open or closed off, conscientious or unconscientious, and neurotic or unneurotic. For each option you may also list 'none' instead of a trait if the story does not represent that trait."
            },
            {
                "role": "user",
                "content": response
            }
        ]
    )
    chat_response = completion.choices[0].message.content
    output.append(chat_response)


df["OpenAI_grade_na"] = output
df.to_csv('personality_data_with_na.csv', index=False)
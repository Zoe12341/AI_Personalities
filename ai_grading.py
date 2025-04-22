# Chat gpt judges personality traits represented
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


#follows_prompt = []
# Adds False if the personality word is explicity listed in the story
def trait_in_response(responses):
    follows_prompt = []
    trait_num = 0
    explicit_traits = ["extroverted", "introverted", "agreeable", "disagreeable", "open", "closed off", "conscientious", "unconscientious", "neurotic", "not neurotic"]
    for response in responses:
        for trait in explicit_traits:
            if trait in response:
                follows_prompt.append("False")
                break
            trait_num += 1
            if trait_num == 5: #been through all traits
                follows_prompt.append("True")
        trait_num = 0
    return follows_prompt

# Only run the following commented out code if updating data
# follows_prompt = trait_in_response(responses)
# df["Follows_Prompt"] = follows_prompt
# df.to_csv('personality_data.csv', index=False)


# # After checking feed responses to Chat GPT for judging
output = []

for response in responses:
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "developer",
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


df["OpenAI_grade"] = output
df.to_csv('personality_data.csv', index=False)

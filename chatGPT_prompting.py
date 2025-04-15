import csv
import os
import pandas as pd


from dotenv import load_dotenv
from openai import OpenAI
client = OpenAI()

load_dotenv()
    
api_key = os.getenv("API_KEY")

df = pd.read_csv('personality_data.csv')
prompts = df.prompt

#df["OpenAI_response"] = None  #Add a column with n/a for all rows
#df.insert(1, 'OpenAI_response', 'n/a')

output = []


for prompt in prompts:
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    chat_response = completion.choices[0].message.content
    output.append(chat_response)


print(output)
df["OpenAI_response"] = output



df.to_csv('personality_data.csv', index=False)






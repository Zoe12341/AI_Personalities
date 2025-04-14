import csv
import os
import pandas as pd

#from openai import OpenAI ChatCompletion
#import openai
from dotenv import load_dotenv
from openai import OpenAI
client = OpenAI()

load_dotenv()
    
api_key = os.getenv("API_KEY")

df = pd.read_csv('personality_data.csv')
prompts = df.prompt

df['OpenAI_response'] = None #Add a column with n/a for all rows

""" for prompt in prompts:
    i = 0
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    df.loc[i, 'OpenAI_response'] = completion.choices[0].message.content
    i +=1 """






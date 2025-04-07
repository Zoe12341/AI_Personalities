import csv
import os

#from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
    
api_key = os.getenv("API_KEY")


"""
client = OpenAI()
"""


""" with open('personality_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        prompt = "Tell a story in less than 250 words about a person who is ___ in openness, ___ in conscientiousness, ___ in extroversion, low in agreeableness, and ___ in neuroticism. Do not use the words agreeable, neurotic, extroverted, open, or conscientious. Rate whether the main character in this story is high or low on each of the big five personality traits: ___story__"
 """
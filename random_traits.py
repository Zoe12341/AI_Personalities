#Python file for randomizing character traits and storing them in personality_data.csv

import random 
import csv

data = [
    ['extraversion', 'agreeableness', 'openness', 'conscientiousness', 'neuroticism', "prompt"]
]
def get_traits():
    extraversion_options = ["extroverted", "introverted"]
    agreeableness_options = ["agreeable", "disagreeable"]
    openness_options = ["open", "closed off"]
    conscientiousness_options = ["conscientious", "unconscientious"]
    neuroticism_options = ["neurotic", "not neurotic"]

    extraversion = random.choice(extraversion_options)
    agreeableness = random.choice(agreeableness_options)
    openness = random.choice(openness_options)
    conscientiousness = random.choice(conscientiousness_options)
    neuroticism = random.choice(neuroticism_options)
    return extraversion, agreeableness, openness, conscientiousness, neuroticism

# Open the CSV file in write mode
with open('personality_data.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the data to the CSV file
    writer.writerows(data)

print("CSV file 'personality_data.csv' created successfully.")


for i in range(20):
    extraversion, agreeableness, openness, conscientiousness, neuroticismm = get_traits()
    prompt = "Tell a story in 3 paragraphs or less about a person who is " + openness + ", " + conscientiousness + ", " + neuroticismm + ", " + agreeableness + ", " + extraversion + ". Do not use the words " + extraversion + ", " + agreeableness + ", " + openness + ", " + conscientiousness + " or, " + neuroticismm

    row_data = [extraversion, agreeableness, openness, conscientiousness, neuroticismm, prompt]
    try:
        with open('personality_data.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(row_data)
    except Exception as e:
        print(f"An error occurred: {e}")




#Python file for randomizing character traits
import random 

extraversion_options = ["extroverted", "introverted"]
agreeableness_options = ["agreeable", "disagreeable"]
openness_options = ["open", "closed off"]
conscientiousness_options = ["concientious", "unconscientious"]
neuroticism_options = ["neurotic", "not neurotic"]

extraversion = random.choice(extraversion_options)
agreeableness = random.choice(agreeableness_options)
openness = random.choice(openness_options)
conscientiousness = random.choice(conscientiousness_options)
neuroticism = random.choice(neuroticism_options)


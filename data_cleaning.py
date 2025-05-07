# File to combine all the dataframes into a single combined data frame combined_df.csv
# The combined dataframe stories information on the intended personality traits, the traits picked up on by human analysis, and models' guess of the intended traits
# It does not need to be run since combined_df.csv is already created

import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns


# # Load CSV files
# chat_gpt = pd.read_csv('personality_data.csv')
# chat_gpt_na = pd.read_csv('personality_data_with_na.csv')

# deepseek_chat = pd.read_csv('deepseek_chat.csv')
# deepseek_chat_na = pd.read_csv('deepseek_chat_na.csv')

# deepseek_reason = pd.read_csv('deepseek_reason.csv')
# deepseek_reason_na = pd.read_csv('deepseek_reason_na.csv')


# #Remove unnecessary columns
# columns_to_drop = [col for col in deepseek_chat.columns if col != 'deepseek_chat_grade']
# deepseek_chat = deepseek_chat.drop(columns=columns_to_drop)

# columns_to_drop2 = [col for col in deepseek_chat_na.columns if col != 'deepseek_chat_grade_na']
# deepseek_chat_na = deepseek_chat_na.drop(columns=columns_to_drop2)

# columns_to_drop3 = [col for col in deepseek_reason.columns if col != 'deepseek_reason_grade']
# deepseek_reason = deepseek_reason.drop(columns=columns_to_drop3)

# columns_to_drop4 = [col for col in deepseek_reason_na.columns if col != 'deepseek_reason_grade_na']
# deepseek_reason_na = deepseek_reason_na.drop(columns=columns_to_drop4)

# columns_to_drop5 = [col for col in chat_gpt.columns if col != 'OpenAI_grade']
# chat_gpt = chat_gpt.drop(columns=columns_to_drop5)


# to_keep = ["extraversion","agreeableness","openness","conscientiousness","neuroticism", "OpenAI_grade_na"]
# columns_to_drop6 = [col for col in chat_gpt_na.columns if col not in to_keep]
# chat_gpt_na = chat_gpt_na.drop(columns=columns_to_drop6)

# combined_df = pd.concat([deepseek_chat, deepseek_chat_na, deepseek_reason, deepseek_reason_na, chat_gpt, chat_gpt_na], axis=1)
# combined_df.to_csv('combined_df.csv', index=False)


# combining human results with the combined_df
# combined_df = pd.read_csv('combined_df.csv')
# human_df = pd.read_csv('human_df.csv')

# human_df["open_mode"] = human_df["open_mode"].replace({1: "open", 0: "closed off"})
# human_df["conscientious_mode"] = human_df["conscientious_mode"].replace({1: "conscientious", 0: "unconscientious"})
# human_df["extravert_mode"] = human_df["extravert_mode"].replace({1: "extroverted", 0: "introverted"})
# human_df["agreeable_mode"] = human_df["agreeable_mode"].replace({1: "agreeable", 0: "disagreeable"})
# human_df["neurotic_mode"] = human_df["neurotic_mode"].replace({1: "neurotic", 0: "unneurotic"})
# combined_df = pd.concat([combined_df, human_df], axis=1)
# combined_df.to_csv('combined_df.csv', index=False)

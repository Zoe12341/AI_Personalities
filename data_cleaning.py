import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns


# # Load CSV files
chat_gpt = pd.read_csv('personality_data.csv')
chat_gpt_na = pd.read_csv('personality_data_with_na.csv')

deepseek_chat = pd.read_csv('deepseek_chat.csv')
deepseek_chat_na = pd.read_csv('deepseek_chat_na.csv')

deepseek_reason = pd.read_csv('deepseek_reason.csv')
deepseek_reason_na = pd.read_csv('deepseek_reason_na.csv')


#Remove unnecessary columns
columns_to_drop = [col for col in deepseek_chat.columns if col != 'deepseek_chat_grade']
deepseek_chat = deepseek_chat.drop(columns=columns_to_drop)

columns_to_drop2 = [col for col in deepseek_chat_na.columns if col != 'deepseek_chat_grade_na']
deepseek_chat_na = deepseek_chat_na.drop(columns=columns_to_drop2)

columns_to_drop3 = [col for col in deepseek_reason.columns if col != 'deepseek_reason_grade']
deepseek_reason = deepseek_reason.drop(columns=columns_to_drop3)

columns_to_drop4 = [col for col in deepseek_reason_na.columns if col != 'deepseek_reason_grade_na']
deepseek_reason_na = deepseek_reason_na.drop(columns=columns_to_drop4)

columns_to_drop5 = [col for col in chat_gpt.columns if col != 'OpenAI_grade']
chat_gpt = chat_gpt.drop(columns=columns_to_drop5)


to_keep = ["extraversion","agreeableness","openness","conscientiousness","neuroticism", "OpenAI_grade_na"]
columns_to_drop6 = [col for col in chat_gpt_na.columns if col not in to_keep]
chat_gpt_na = chat_gpt_na.drop(columns=columns_to_drop6)

combined_df = pd.concat([deepseek_chat, deepseek_chat_na, deepseek_reason, deepseek_reason_na, chat_gpt, chat_gpt_na], axis=1)
combined_df.to_csv('combined_df.csv', index=False)
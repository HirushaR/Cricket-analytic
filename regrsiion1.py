import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/Men ODI Player Innings Stats - 21st Century.csv')


player_Name = 'KC Sangakkara'


df.rename(columns={'Innings Player':'Name',
                   'Innings Runs Scored Num': 'score'
                   },inplace=True)

df = df[['Name','score']]
df = df.loc[df['Name'] == player_Name]
df.dropna(inplace=True)
df['score'] = df['score'].str.replace('\-','0')
df['score'] = df['score'].astype('float')
print(df.groupby('Name').sum())




# print(group)
# Player = df['Name'].unique()
# plt.bar(Player, group['score'])
# plt.xticks(Player,rotation='vertical',size=5)
# plt.ylabel('scores')
# plt.xlabel('player Name')
# plt.show()
#
#

import pandas as pd

df = pd.read_csv('data/Men ODI Player Innings Stats - 21st Century.csv')


df.rename(columns={'Innings Player':'Name',
                   'Innings Runs Scored Num': 'score'
                   },inplace=True)

df2 = df[['Name','score']]
df2.fillna(0)
df2["score"] =df2["score"].replace(r'DNB','0')
df2["score"] =df2["score"].replace(r'TDNB','0')
df2["score"] =df2["score"].replace(r'^0-9a-zA-Z','0')
df2['score'] = df2['score'].str.replace('\-','0')

df2['score'] = df2['score'].astype('float')



# print(df2.replace(r'\$-','0').astype(float))
print(df2.groupby('Name',sort=False)['score'].sum().reset_index())















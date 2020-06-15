import pandas as pd
import matplotlib.pyplot as plt

#read the file
df = pd.read_csv('data/Men ODI Player Innings Stats - 21st Century.csv')

#player name
player_Name = 'JJ Roy'

#rename the column
df.rename(columns={'Innings Player':'Name',
                   'Innings Runs Scored Num': 'score'
                   },inplace=True)

#set the new dataframe
df = df[['Name', 'score', 'Opposition', 'Innings Date']]

# Add the year column
#df['year'] = pd.DatetimeIndex(df['Innings Date']).year
df['year'] = pd.to_datetime(df['Innings Date']).dt.strftime('%Y')

##################################### cleaning ##################################################

#get the single player data according to his name
df = df.loc[df['Name'] == player_Name]

#clean the data set
df.dropna(inplace=True)
df['score'] = df['score'].str.replace('\-','0')
df['score'] = df['score'].astype('float')

#change the data of opponent column
def get_Opponent(opponent):
    return opponent.split('v')[1]

df['team'] = df['Opposition'].apply(lambda x: get_Opponent(x))


###################### grouping ############################################################

#get player score with each country
teams = df.groupby('team')
years =df.groupby('year')
#get total
team_score = df.groupby('team').sum()
#get avarage
avg_score = df.groupby('team').mean()
#get  by year
years_score = df.groupby('year').sum()
avg_year =df.groupby('year').mean()


###################################### ploting ##################################################
team = [team for team, df in teams]
year = [year for year, df in years]

#dual ploting
#plot score with team and plot avarage with team
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.bar(team,team_score['score'],color='g')
ax2.plot(team,avg_score,'b-')

ax1.set_ylabel('Scores')
ax1.set_xlabel('Team', color='g')
ax2.set_ylabel('Average', color='b')
ax1.set_xticklabels(team, rotation='vertical',size=5)
plt.show()


#single ploting
# plt.bar(year , years_score['score'])
# plt.ylabel('scores')
# plt.xlabel('Years')
# plt.show()

# plot year score with year and year avarage with year
fig2, axx1 = plt.subplots()
axx2 = axx1.twinx()

axx1.bar(year,years_score['score'],color='g')
axx2.plot(year,avg_year,'b-')

axx1.set_ylabel('Scores')
axx1.set_xlabel('Year', color='g')
axx2.set_ylabel('Average', color='b')
axx1.set_xticklabels(year, rotation='vertical',size=5)
plt.show()









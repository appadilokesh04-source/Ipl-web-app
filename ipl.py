import pandas as pd
import numpy as np
ipl_matches ="https://editorial.uefa.com/resources/028d-1ae29d7959f7-e4ad8bfe761e-1000/euro_2024_match_schedule.pdf"
matches=pd.read_csv(ipl_matches)
print(matches.head())
def teamsAPI():
    teams=list(set(list(matches['Team1'])+list(matches['Team2'])))
    team_dict={
        'teams':teams
    }
    return team_dict
def teamvteamAPI(team1,team2):
    valid_teams=list(set(matches['Team1'])+list(matches['Team2']))
    if team1 in valid_teams and team2 in valid_teams:
      temp_df=matches[(matches['Team1']==team1)&(matches['Team2']==team2)] | (matches['Team1']==team2)&(matches['Team2']==team1)
      total_matches=temp_df.shape[0]
      matches_won_team1=temp_df['WinningTeam'].value_counts()[team1]
      matches_won_team2=temp_df['WinningTeam'].value_counts()[team2]
      draws=total_matches-(matches_won_team1+matches_won_team2)
    response={
        'total_matches':total_matches,
        team1:matches_won_team1,
        team2:matches_won_team2,
        'draws':draws
    }
    return response
# import des module
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import teams
from nba_api.stats.static import players
import pandas as pd
import numpy as np
import boto3

###  Players names and id
nba_players=players.get_players()
# Retrieving all names and ids in a dictionary
players_ids= {"id":[],"full_name":[],"first_name":[],"last_name":[],"is_active":[]}

for player in nba_players:
    players_ids["id"].append(player["id"])
    players_ids["full_name"].append(player["full_name"])
    players_ids["first_name"].append(player["first_name"])
    players_ids["last_name"].append(player["last_name"])
    players_ids["is_active"].append(player["is_active"])
players_ids=pd.DataFrame(players_ids)

# Checking the first 5 rows
players_ids.head()

# saving file
players_ids.to_csv('players_ids.csv') 

### Actives Players stats
# Retrieving all plyers id from the players_ids where is_active is True
ids_temps=players_ids[players_ids["is_active"]==True]
ids=ids_temps["id"].values
# Boucle pour récupérer les données de chaque joueur
res=[]
for i in ids:
    career = playercareerstats.PlayerCareerStats(player_id=i) 
    t = career.get_data_frames()[0]
    res.append(t)
# concatenation des données
playeur_stat = pd.concat(res, ignore_index=True)

# saving file
playeur_stat.to_csv('active_playeur_stat.csv') 

### Retired Players stats
# Retrieving all plyers id from the players_ids where is_active is False
ids_temps=players_ids[players_ids["is_active"]==False]
ids=ids_temps["id"].values

# Boucle pour récupérer les données de chaque joueur
res=[]
for i in ids:
    career = playercareerstats.PlayerCareerStats(player_id=i) 
    t = career.get_data_frames()[0]
    res.append(t)
# concatenation des données
playeur_stat = pd.concat(res, ignore_index=True)

# saving file
playeur_stat.to_csv('retired_playeur_stat.csv')


### NBA Teams names
nba_teams = teams.get_teams()
# Retrieving all names and ids in a dictionary
teams_ids= {"id":[],"full_name":[],"abbreviation":[],"nickname":[],"city":[],"state":[],"year_founded":[]}

for team in nba_teams:
    teams_ids["id"].append(team["id"])
    teams_ids["full_name"].append(team["full_name"])
    teams_ids["abbreviation"].append(team["abbreviation"])
    teams_ids["nickname"].append(team["nickname"])
    teams_ids["city"].append(team["city"])
    teams_ids["state"].append(team["state"])
    teams_ids["year_founded"].append(team["year_founded"])
teams_ids=pd.DataFrame(teams_ids)

# Saving file
teams_ids.to_csv('teams_ids.csv') 
# import libraries
import requests
import pandas as pd 
import json
from datetime import datetime
import s3fs 
import numpy as np
 
# Test Rapid API NBA

url = "https://api-nba-v1.p.rapidapi.com/teams"

headers = {
	"X-RapidAPI-Key": "d9325a7754msh77677957c817a38p1b23eejsn00bfc46e1e01",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

#Cleaning
data=response.json()
data=data['response']
stock={"id":[],"team_names":[],"city":[],"nba_franchise":[],"Conference":[],"division":[],"code":[]}
for i in range(len(data)):
    stock['id'].append(data[i]['id'])
    stock['team_names'].append(data[i]['name'])
    stock["city"].append(data[i]['city'])
    stock["nba_franchise"].append(data[i]['nbaFranchise'])
    stock['code'].append(data[i]['code'])
    # Vérification de l'existence de la clé 'leagues' et de 'standard' avant d'accéder à 'conference'
    if 'leagues' in data[i] and 'standard' in data[i]['leagues']:
        stock['Conference'].append(data[i]['leagues']['standard'].get('conference', 'NA'))
    else:
        stock['Conference'].append('NA')

    if 'leagues' in data[i] and 'standard' in data[i]['leagues']:
        stock['division'].append(data[i]['leagues']['standard'].get('division', 'NA'))
    else:
        stock['division'].append('NA')
data_team=pd.DataFrame(stock)
data_team=data_team.query("nba_franchise == True")
data_team = data_team.query("team_names != 'Home Team Stephen A'")
data_team['false_min_played'] = np.random.normal(loc=278.5, scale=78.5, size=len(data_team))
data_team['false_game_played'] = np.random.randint(low=82, high=91, size=len(data_team))
data_team.to_csv('data_team_finaless.csv') 
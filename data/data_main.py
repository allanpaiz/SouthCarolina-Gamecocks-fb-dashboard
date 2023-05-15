from data_utils import standings
import json
import pandas as pd
import re

def load_raw_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main_team_info(raw_data):
    df = raw_data[0]['Team Info']
    teamName = df[0]
    logo = df[1]
    conference = df[2]['Conference'] + ')'
    coach = df[2]['Coach']

    return teamName, logo, conference, coach

def prev_season_sum(raw_data):
    df = raw_data[0]['Team Info']
    record = df[2]['Record'] + ')'
    conferenceRecord = df[2]['Conference Record']
    pointsFor = df[2]['Points For']
    pointsAgainst = df[2]['Points Against']
    sos = df[2]['SOS']

    return record, conferenceRecord, pointsFor, pointsAgainst, sos

def conference_standings(dict):
    df = pd.DataFrame(data = dict)
    return df

def schedule_ranking_data(raw_data):
    sr = {
        'Team Name' : [],
        'Points For' : [],
        'Points Against' : [],
        'Points Per Game' : [],
        'Points Allowed Per Game' : [],
        'SOS' : []
    }

    for i in range(len(raw_data)):
        if raw_data[i] is not None:
            df = raw_data[i]['Team Info']
            teamName = df[0]

            try:
                pointsFor = int(df[2]['Points For'])
                pointsAgainst = int(df[2]['Points Against'])
                pointsPerGame = float(re.search(r'\d+(\.\d+)?', df[2]['Points/G']).group())
                pointsAllowedPerGame = float(re.search(r'\d+(\.\d+)?', df[2]['Opp Pts/G']).group())
                sos = float(re.search(r'\d+(\.\d+)?', df[2]['SOS']).group())
            except IndexError:
                pointsFor = pointsAgainst = pointsPerGame = pointsAllowedPerGame = sos = None

            sr['Team Name'].append(teamName)
            sr['Points For'].append(pointsFor)
            sr['Points Against'].append(pointsAgainst)
            sr['Points Per Game'].append(pointsPerGame)
            sr['Points Allowed Per Game'].append(pointsAllowedPerGame)
            sr['SOS'].append(sos)

    df = pd.DataFrame(data = sr)
    return df

data = load_raw_data('C:/Users/allan/OneDrive/Documents/00LIFE/Projects/GameCocks/data/raw_data.json')
teamName, logo, conference, coach  = main_team_info(data)
conferenceStanding = conference_standings(standings)
scheduleData = schedule_ranking_data(data)
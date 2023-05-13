import json
import time
from scraper_tools import *
from scraping_utils import *

def single_team(url):
    teaminfo = team_info(url)
    overallstats = ovr_team_stats(url)
    gamelogs = game_logs(url)
    return {'Team Info': teaminfo, 'Overall Stats': overallstats, 'Game Logs': gamelogs}

def store_data(data, file_name):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)

def main():
    link_list = [game[3] for game in schedule]

    all_data = []
    for link in link_list:
        if link is None:
            all_data.append(None)
            continue  # Skip the current iteration if the link is None

        all_data.append(single_team(link))
        time.sleep(60)  # Add a one-minute delay here

    store_data(all_data, 'data.json')
    print("Data scraping and storage completed.")

if __name__ == "__main__":
    main()
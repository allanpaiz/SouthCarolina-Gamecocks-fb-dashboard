from scraping_utils import *
import requests
from bs4 import BeautifulSoup

def team_info(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('title').text
    team_name = title.split('2022 ')[1].split(' Stats')[0]

    team_n = url_splitter(base_url)
    logo_url = f'https://cdn.ssref.net/req/202305101/tlogo/ncaa/{team_n}.png'
    logo_filename = f'{team_name.lower().replace(" ", "_")}_logo.png' 
    download_logo(logo_url, logo_filename)

    data_keys = ["Coach", "Points For", "Points/G", "Points Against", "Opp Pts/G", "SRS", "SOS"]
    summary_info = {key: None for key in data_keys}

    for tag in soup.find_all('p'):
        text = tag.get_text()

        # Handle Record, Conference, and Conference Record separately
        if "Record" in text and "Conference Record" not in text:
            summary_info['Record'] = text.split(")")[0].split(":")[1].strip()

        if "Conference" in text and "Conference Record" not in text:
            summary_info['Conference'] = text.split("Conference:")[1].split(")")[0].strip()

        if "Conference Record" in text:
            summary_info['Conference Record'] = text.split("Conference Record:")[1].split(")")[0].strip()

        for key in data_keys:
            if key in text:
                summary_info[key] = text.split(":")[1].strip()
                break

    return team_name, logo_filename, summary_info

def ovr_team_stats(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'lxml')
    over_header = [i.text.strip() for i in soup.find_all('th', attrs={'class': 'over_header center'})]
    poptip = [i.text.strip() for i in soup.find_all('th', attrs={'scope': 'col'})]
    row_names = [i.text.strip() for i in soup.find_all('th', attrs={'class': 'left'})]
    row_values = make_nested_list([i.text.strip() for i in soup.find_all('td', attrs={'class': 'right'})], 22)
    team_stats = {'Over Headers': over_header, 'Headers': poptip, 'Row Names': row_names, 'Values': row_values}
    return team_stats

def game_logs(base_url):
    game_logs_url = base_url[:-5] + '/gamelog/'
    response = requests.get(game_logs_url)
    soup = BeautifulSoup(response.content, 'lxml')

    headers = [i.text.strip() for i in soup.find_all('h2')]
    over_header = [i.text.strip() for i in soup.find_all('th', attrs={'class': 'over_header center'})]
    poptip = [i.text.strip() for i in soup.find_all('th', attrs={'scope': 'col'})]
    gameid = [i.text.strip() for i in soup.find_all('th', attrs={'scope': 'row'})]
    offense = make_nested_list([i.text.strip() for i in soup.find_all('td')], 25)
    defense = make_nested_list(clean_defense(soup.find_all('div', attrs={'id': 'all_defense'})), 25)

    game_logs = {'Table Names': headers[0:2], 'Over Headers': over_header, 'Headers': poptip, 'Game': gameid, 'Offense Data': offense, 'Defense Data': defense}
    return game_logs

def single_team(base_url):
    teaminfo = team_info(base_url)
    overallstats = ovr_team_stats(base_url)
    gamelogs = game_logs(base_url)
    return {'Team Info': teaminfo, 'Overall Stats': overallstats, 'Game Logs': gamelogs}
import time
from scraper_tools import *
from scraping_utils import *

def main():
    link_list = [game[3] for game in schedule]

    all_data = []
    for link in link_list:
        if link is None:
            all_data.append(None)
            continue

        all_data.append(single_team(link))
        time.sleep(60)

    store_data(all_data, 'data.json')
    print("Data scraping and storage completed.")

if __name__ == "__main__":
    main()
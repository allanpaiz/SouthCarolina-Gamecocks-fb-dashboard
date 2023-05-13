import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

def download_logo(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(filename)

def url_splitter(url):
    return url.split('/')[5]

def clean_defense(data):
    string = str(data[0]).split('<!--')[1].split('-->')[0]
    soup = BeautifulSoup(string, 'lxml')
    return [i.text.strip() for i in soup.find_all('td')]

def make_nested_list(data, n):
    return [data[i:i+n] for i in range(0, len(data), n)]

schedule = [
    (1, 'Sat Sep 2', 'vsNorth Carolina', 'https://www.sports-reference.com/cfb/schools/north-carolina/2022.html'),
    (2, 'Sat Sep 9', 'vsFurman', None),
    (3, 'Sat Sep 16', '@Georgia', 'https://www.sports-reference.com/cfb/schools/georgia/2022.html'),
    (4, 'Sat Sep 23', 'vsMississippi State', 'https://www.sports-reference.com/cfb/schools/mississippi-state/2022.html'),
    (5, 'Sat Sep 30', '@Tennessee', 'https://www.sports-reference.com/cfb/schools/tennessee/2022.html'),
    (6, 'Sat Oct 14', 'vsFlorida', 'https://www.sports-reference.com/cfb/schools/florida/2022.html'),
    (7, 'Sat Oct 21', '@Missouri', 'https://www.sports-reference.com/cfb/schools/missouri/2022.html'),
    (8, 'Sat Oct 28', '@Texas A&M', 'https://www.sports-reference.com/cfb/schools/texas-am/2022.html'),
    (9, 'Sat Nov 4', 'vsJacksonville State', None),
    (10, 'Sat Nov 11', 'vsVanderbilt', 'https://www.sports-reference.com/cfb/schools/vanderbilt/2022.html'),
    (11, 'Sat Nov 18', 'vsKentucky', 'https://www.sports-reference.com/cfb/schools/kentucky/2022.html'),
    (12, 'Sat Nov 25', 'vsClemson', 'https://www.sports-reference.com/cfb/schools/clemson/2022.html')
]
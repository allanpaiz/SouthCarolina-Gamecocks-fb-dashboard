# South Carolina Gamecocks Football Dashboard

An interactive dashboard for visualizing and analyzing football statistics for the University of South Carolina Gamecocks, built using Python, Plotly, and Flask.

## Dependencies

This project requires the following libraries:

- beautifulsoup4
- pandas
- plotly
- Flask
- requests

To install the dependencies, run the following command:

```
pip install -r requirements.txt
```


## Setup

1. Clone the repository:

```
git clone https://github.com/allanpaiz/SouthCarolina-Gamecocks-fb-dashboard.git
cd SouthCarolina-Gamecocks-fb-dashboard
```

2. Run the scrapers to collect data:

```
python scraper/scraper_main.py
```

## Updates

### May 18, 2023 - First Update.
I should have started this update thing a while ago. But here we are. 

#### Where I'm At:
- Scraper : 75% - Needs a few additions, and code refactoring  
- Data Cleaning : 85% - Needs a lot of code refactoring, I've completed the initial draft of the code and now I'm optimizing it for readability and performance, which includes standardizing naming conventions, managing white space, adding comments, and so forth.
- Analysis : 20% - I've figure out how I want to analyze and give 'Potential Exploits'. I revisited the design of the page, given what I know now. 
- Dashboard : 5% - I've set up the Flask, HTML, and CSS code and files to start implementing the design. Not knowing HTML and CSS is a huge hurdle. 

#### Highlights
- Made my [first three visualizations](https://github.com/allanpaiz/SouthCarolina-Gamecocks-fb-dashboard/tree/main/vis/FirstDraft) using python and plotly, by first I mean, one that I am happy with putting out to the world. They need some fixes, but finally getting it all to work was a good feeling.

![ppg_sos](https://github.com/allanpaiz/SouthCarolina-Gamecocks-fb-dashboard/blob/main/vis/FirstDraft/ppg_sos.png)

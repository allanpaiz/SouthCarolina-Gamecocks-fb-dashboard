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

***

## Updates
Weekly Updates (Sorted by Most Recent):
1. [May 24, 2023](https://github.com/allanpaiz/SouthCarolina-Gamecocks-fb-dashboard#may-24-2023)
2. [May 18, 2023 - First Update](https://github.com/allanpaiz/SouthCarolina-Gamecocks-fb-dashboard#may-18-2023---first-update)

***

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

***

### May 24, 2023
- General : This week has been slow in terms of progress, and it will slow down signinficantly this coming week. Which is why I am posting a day eariler. A lot of time was spent refactoring and rethinking some things for the scraper portion of this project. I finished what I'm calling the 'skeleton' of the analysis portion. Happy with my approach, although it may not be the smartest approach. 

#### Where I'm At:
- Scraper : 90% [+15%] - A lot of code refactoring is comeplete. Almost to the point of completing this section, and tying it in well with everythign else.  
- Data Cleaning : 85% - No Change.
- Analysis : 65% [+45%] - Code Skeleton is done. Now just need to do a lot of code refactoring, and revisit some things as I come back to this.
- Dashboard : 5% - No Change

### Highlights
- As mentioned above my analysis portion of this project in terms of the basework is complete. There's a lot of things that need to be revisited or re-worked. But I know I have good foundation, for when I come back and start prepping everything for the dashboard. 

This is what the analysis outputs currently, in a terminal. I'm happy with how its comming along so far, it may not seem like a lot and thats by design, but behind the scenes a lot has gone into this output. 

![analysis_draft](https://github.com/allanpaiz/SouthCarolina-Gamecocks-fb-dashboard/blob/main/vis/FirstDraft/analysis_draft.png)

### Next Steps
- Continue working on code refactoring and prepping the Scraper for publication. As the scraper is complete, and fine tuned with the Data Cleaning modules, I think progress will slow down with the refactoring of the Analysis module. I'm learning a lot as I go, and I'm excited to start learning how to implement everything into the dashboard. 

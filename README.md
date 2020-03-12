# ECE143-Team 13
Analysis of Uber &amp; Lyft prices

# Authors
*Jiayuan Shen
*John Xie
*Robert Young
*Jialu Zhao

# Presentation
You can view our presentation by click here https://github.com/jacinda96/ECE143/blob/master/ECE_143_Final_Project_%5B13%5D.pdf

# File Structure
```
uber-lyft-cab-prices/
    cab_rides.csv
    weather.csv
chart/
    Lyft Avg Price During Day vs Day of Week.png
    Lyft Price per Mile vs Cab Type.png
    Lyft Price per mile vs rain.png
    Lyft Price per mile vs wind.png
    Lyft_price_network.png
    Uber Avg Price During Day vs Day of Week.png
    Uber Price per Mile vs Cab Type.png
    Uber Price per mile vs rain.png
    Uber Price per mile vs wind.png
    Uber_price_network.png
    boston_map.png

code/
    Data_processing.py
    Data_distribution.py
    Map_visualization.py
    Price_prediction.py
    graph_visualization.py
    UL_Visualization.py
    
Data/
    data_merged.csv.zip
    data_test.csv

ECE143.ipynb
ECE143_143_Final_project_[13].pdf
README.md
```

# How to run our Data

# Data Collection

We used kaggle as our primary dataset as it was the best and most relevant source we could find to our topic
This dataset was used to form the basis of our data analysis visualizations and used by our machine learning 
algorithms.
Kaggle Dataset: https://www.kaggle.com/ravi72munde/uber-lyft-cab-prices

Manual Data

In addition to the above dataset, we also collected similar data manually using the Uber and Lyft apps from the apple store.
The purpose of this was to create a test set for our machine learining models for price prediction against.

Our data collection followed the pattern manually entering in price of ride requests for both apps 
according to the google sheets linked below. This google sheets was constructed to model the exect
same datapoints found in the original kaggle dataset. For ride prices, times were collected starting at the hour(s)
of 7am, 11am, and 3pm with the goal of collecting all data within the same hour and with routes corresponding to every route instance found in the kaggle dataset. For weather, data was collected once for every location in the dataset for the same time periods. This process was repreated everyday for a week to collect a comparable dataset to the kaggle data.

NOTE: Cab types were randomly chosen for any given query.

Data : https://docs.google.com/spreadsheets/d/1ADEPHjSxZHUB_ZmmxWcxfHpzXunH4R7EzefOCRVzXtg/edit?usp=sharing

## Start up Jupter Notebook
Open ECE143.ipynb in Jupter Notebook and run from the first cell. 
You need to unzip the data_merged.csv.zip first before running our code.

# Third Party modules
```
pandas
datetime
numpy
plotly
matplotlib
psutil
pylab
seaborn
networkx
math
sklearn
```


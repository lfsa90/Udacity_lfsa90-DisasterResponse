# Disaster Response Pipeline Project

This code was written under the Udacity Data Scientist Nanodegree Project.

## Table of Contents

1. [Installation](#Installation)
2. [Data](#Data)
3. [Results](#Results)
4. [Licensing, Authors, and Acknowledgements](#Licensing)

## Installation <a name="Installation"></a>
* The code was developed and tested on anaconda with python 3.73. Nevertheless, it should run with no issues using Python 3.* in any other environment.
* The following packages must be installed:
  *nltk (additional packages will automatically be downloaded once the main routine is executed)
  *flask
  *plotly
 
## Data <a name="Data"></a>
```text
./
├── DataScience-LisbonAirbnb.ipynb
├── utility.py
└── data/
    ├── listings_complete.csv
    ├── calendar.csv
    ├── listings.csv
```
* __DataScience-LisbonAirbnb.ipynb__: Notebook with all the scripts used to analyse data and to answer the questions mentioned above
* __Data/listings.csv__: Listings data for Lisbon ([Airbnb](https://airbnb.com/))
* __Data/listings_complete.csv__: Detailed Listings data for Lisbon ([Airbnb](https://airbnb.com/))
* __Data/calendar.csv__: Detailed Calendar Data for listings in Lisbon ([Airbnb](https://airbnb.com/))

## Results <a name="Results"></a>
The detailed analysis and main conclusions/results are availabe in [here](https://medium.com/@luisf.almeida90/lisbon-an-amazing-destination-b36edff06967)).

* Price fluctuation over time

![price_vs_time](price_vs_time.png)
For 2019, the prices decrease after Summer time until December.
Then, close to New Year's Eve, there is sudden increase in average price as it would be expected.
For 2020, the prices are considerably higher than in 2019, and seem to steadily increase from the begining of the year.


* Listings - price tag and property types

![pricetag](pricetag.png)

![proptype](proptype.png)

As seen in the bar chart above, most of the listings have a price tag between 20\\$ and 140\\$
Also, the most frequent property type is apartment, followed up by (entire) house.


* Main factors influencing price

![pricepred](pricepred.png)

The features which characterize the house/listing topology (bathrooms, bedrooms, accomodates) are on the top 5 of the top 10 important features, meaning these features have a high impact on the price.


## Licensing, Authors, and Acknowledgements <a name="Licensing"></a>
* Thanks to Udacity for all the useful insights and interesting challenges!
* Thanks to Airbnb for making these data sets available to everyone!



### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

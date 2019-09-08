# Disaster Response Pipeline Project

This code was written under the Udacity Data Scientist Nanodegree Project.

## Table of Contents

1. [Installation](#Installation)
2. [Introduction / Motivation](#Motivation)
3. [Data](#Data)
4. [Results](#Results)
5. [Instructions](#Instructions)
6. [Licensing, Authors, and Acknowledgements](#Licensing)

## Installation <a name="Installation"></a>
* The code was developed and tested on anaconda with python 3.73. Nevertheless, it should run with no issues using Python 3.* in any other environment.
* The following packages must be installed:
  * nltk (additional packages will automatically be downloaded once the main routine is executed)
  * flask
  * plotly
  
* Clone this GIT repository:
```
git clone https://github.com/matteobonanomi/disaster-response.git
```
 
## Introduction / Motivation <a name="Motivation"></a>
This is an Udacity Data Science Nanodegree project.
The aim is apply Natural Language Processing tools 

How does price fluctuate over time?;
What is the availability trend over time?;
What type of listings do we have in Lisbon? - price range, house types and listings by neighbourood;
How is availability related wity price, host type, number of reviews and scores, and room type?;
Price preditction - main factors influencing price.
 
## Data <a name="Data"></a>
```text
Udacity_lfsa90-DisasterResponse/
└── app/
    └── templates/
        ├── go.html
        ├── main.html
    ├── run.py
└── data/
    ├── DisasterResponce.db
    ├── disaster_categories.csv
    ├── disaster_messages.csv
    ├── process_data.py
└── models/
    ├── train_classifier.py
    ├── classifier.pkl
    
```
1) app
  * _templates_: html files for the web application
  * _run.py_: file to run the web app
2) data
  * _disaster_categories.csv_: dataset including all the categories
  * _disaster_messages.csv_: dataset including all the messages
  * _process_data.py_: python script (ETL pipeline) to read, clean and save data into a database
  * _DisasterResponse.db_: output of _process_data.py_ (SQLite database with cleansed data)
3) models
  * _train_calssifier.py_: python script to build Machine Learning pipeline. The ouput is the classifier in a pickle file
  * _classifier.pkl_: output of _train_classifier.py_ (trained classifier to classify new messages)
 

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

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


## Licensing, Authors, and Acknowledgements <a name="Licensing"></a>
* Thanks to Udacity for all the useful insights and interesting challenges!
* Thanks to Airbnb for making these data sets available to everyone!


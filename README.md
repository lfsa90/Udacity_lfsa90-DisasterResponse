# Disaster Response Pipeline Project

This code was written under the Udacity Data Scientist Nanodegree Project.

## Table of Contents

1. [Installation](#Installation)
2. [Introduction / Motivation](#Motivation)
3. [Data](#Data)
4. [Screenshots](#Screenshots)
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
git clone https://github.com/lfsa90/Udacity_lfsa90-DisasterResponse.git
```
 
## Introduction / Motivation <a name="Motivation"></a>
This is an Udacity Data Science Nanodegree project.
The aim of this project is to apply Natural Language Processing and Machine Learning in building a model capable of automatically classify disaster messages (messages shared by people during disasters) - the dataset was provided by Figure Eight.
The final result is a web application that enables a user to type in a certain sentence and check the corresponding category in real time (model output).
 
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
 

## Screenshots <a name="Screenshots"></a>


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
* Thanks to Figure Eight for making these data sets available.


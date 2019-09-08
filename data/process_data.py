import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''
        Load Data Function - loading data sets

        Arguments:
            messages_filepath - path to messages file (messages.csv)
            categories_filepath - path to categories file (categories.csv)
        Output:
            df - dataframe with merged datasets (messages & categories)
    '''

    # load messages dataset
    messages = pd.read_csv(messages_filepath)

    # load categories dataset
    categories = categories = pd.read_csv(categories_filepath)

    # merge datasets
    df = pd.merge(messages, categories, on='id')

    return df

def clean_data(df):
    '''
        Clean Data Function - cleaning dataframe (extrating categories names, updating dataframe, removing duplicates)

        Arguments:
            df - dataframe with merged raw datasets (messages & categories)
        Output:
            df - cleaned dataframe
    '''

    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(";", expand=True)

    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # extracting a list of new column names for categories
    row = row.apply(lambda x: x[:-2])

    # rename the columns of `categories`
    categories.columns = row

    # converting category values to just numbers 0 or 1
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]

        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])

    # replacing categories column in df with new category columns
    # drop the original categories column from `df`
    df.drop(['categories'], axis=1, inplace=True)

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)

    # removing duplicates
    # check number of duplicates
    df.duplicated(subset=['id']).sum()

    # drop duplicates
    df.drop_duplicates(subset=['id'], keep='first', inplace=True)

    # returning cleaned dataframe
    return df

def save_data(df, database_filename):
    '''
        Save data Function - saving cleaned data to a database

        Arguments:
            df - cleaned data set (merged categories & messages)
            database_filename - filepath to save the database
        Output:
            NA
    '''

    name = 'sqlite:///' + database_filename
    engine = create_engine(name)
    df.to_sql('DisasterResponse', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
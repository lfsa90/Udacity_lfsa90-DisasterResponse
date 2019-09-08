# General
import sys
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import pickle
import re

# Scikit
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV

# download necessary NLTK data
import nltk
nltk.download('stopwords')
nltk.download(['punkt', 'wordnet'])
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def load_data(database_filepath):

    '''
        Load data Function - loading data from database

        Arguments:
            database_filename - filepath to load the database
        Output:
            X - messages
            Y - categories
            category_names - categories' names
    '''

    # Loading data
    name = 'sqlite:///' + database_filepath
    engine = create_engine(name)
    df = pd.read_sql_table('DisasterResponse', engine)

    # Spliting dataset into messages ('X') and categories ('y')
    X = df['message']
    Y = df.iloc[:, 4:]
    category_names = list(df.columns[4:])

    return X, Y, category_names


def tokenize(text):

    '''
        tokenize Function - cleaning raw text (normalization, stop words, stemming).

        Arguments:
            text - raw text to be cleaned
        Output:
            stemmed - cleaned and stemmed text
    '''

    # Case normalization
    text = text.lower()

    # Remove punctuation characters
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)

    # Split text into words using NLTK - Tokenization
    words = word_tokenize(text)

    # Remove stop words
    words = [w for w in words if w not in stopwords.words("english")]

    # lemmatize
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for tok in words:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)
    return clean_tokens

def build_model():

    '''
        build model Function - build ML pipeline for text classification (multi output)

        Arguments:
            NA
        Output:
            cv - ML pipeline for text classification, optimized with gridsearchCV
    '''
    
    # ML pipeline 
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    # parameters for gridsearchCV
    parameters = {'clf__estimator__n_estimators': [5, 10]
                  #,'clf__estimator__min_samples_split': [2, 3]
                  #,'clf__estimator__criterion': ['entropy', 'gini']
                 }
    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    return cv


def evaluate_model(model, X_test, Y_test, category_names):

    '''
        evaluate model Function - evaluate model performance on testing set

        Arguments:
            model - ML model (pipeline) to be evaluated
            X_test - test set (messages)
            Y_test - test set (output/categories)
            category_names - categories (names)
        Output:
            NA
    '''

    # predict on test data
    y_pred = model.predict(X_test)

    # Full report
    print ("-> Full report:")
    for i in range(len(category_names)):
        print("Category:", category_names[i], "\n", classification_report(Y_test.iloc[:, i].values, y_pred[:, i]))
        print('Accuracy of %25s: %.2f' % (category_names[i], accuracy_score(Y_test.iloc[:, i].values, y_pred[:, i])))

    # Accuracy only
    accuracy = (y_pred == Y_test).mean()
    print("\n\n-> Accuracy:", accuracy)

def save_model(model, model_filepath):

    '''
        save model Function - saving trained model to a picle file

        Arguments:
            model - ML model (pipeline) to be saved
            model_filepath - filepath to save picle file (with trained model)
        Output:
            NA
    '''

    # Saving model
    pickle.dump(model, open(model_filepath, "wb"))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from plotly.graph_objs import Pie
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('DisasterResponse', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    category_names = df.iloc[:,4:].columns
    category_checking = (df.iloc[:,4:] != 0).sum().values
    origin = df.iloc[:,3].values
    
    cat_counts = df[df.columns[5:]].mean()*df[df.columns[5:]].shape[0]
    large_counts = cat_counts.nlargest(3)
    large_names = list(large_counts.index)
    
    small_counts = cat_counts.nsmallest(3)
    small_names = list(small_counts.index)
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
         {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        # additional  
        {
            'data': [
                Bar(
                    x=category_names,
                    y=category_checking
                )
            ],
            'layout': {
                'title': 'Messages per category names',
                'yaxis': {
                    'title': "Category Name"
                },
                'xaxis': {
                    'title': "Count",
                    'tickangle': 45
                }
            }
        },
       # additional  
        {
            'data': [
                Bar(
                    x=large_names,
                    y=large_counts
                )
            ],
            'layout': {
                'title': 'Top 3 categories by messages count',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Category Name",
                    'tickangle': 45
                }
            }
        },
        # additional  
        {
            'data': [
                Pie(
                    labels=category_names,
                    values=category_checking
                )
            ],
            'layout': {
                'title': 'Categories distribution - pie chart view',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Category Name",
                    'tickangle': 45
                }
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
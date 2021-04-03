# -*- coding: utf-8 -*-


# Global Path & other utilities
from utils import *

# preprocessing file
from preprocess import Preprocessing_mod

# DB Loading live streaming
from StreamWikiSQL import *

# common imports
import time
import sqlite3  
import argparse                                
import pandas as pd
import plotly.graph_objs as go

# Dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate



# Call the DB Live stream Class
# streamer_class  = WikiEventStreamer(url = 'https://stream.wikimedia.org/v2/stream/recentchange', run_time = None)
# streamer_class.stream_wiki_data()


metrics_updation_time = 4
app = dash.Dash(__name__)


app.layout = html.Div(
    [   html.H2('Wikipedia Streaming Application (Edits)'),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval    = 4 * 1000,
        ),
    ]
)


@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])

def update_graph(n):
    try:
        conn             = sqlite3.connect(DB_SAVED)
        c                = conn.cursor()
        df               = pd.read_sql("SELECT * FROM WikiEventStreams", conn)
        df               = df.loc[-30000:].reset_index(drop= True)
        preprocess_cls   = Preprocessing_mod(df, None)
        df, df_final     = preprocess_cls.main_func()
        X                = df_final.Date_hour_min.values
        Y                = df_final.all_lang_qty.values
           
        data = go.Scatter(
            x            = X,
            y            = Y,
            text         = Y, 
            textposition = "top right", 
            textfont     = dict(size=12), 
            mode         ='lines+markers+text',
            line         = dict(width = 3, dash = 'dot'), 
            marker       = dict(color= 'red', size= 20),
            )
                

        return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                    yaxis=dict(range=[min(Y),max(Y)]),
                                                    yaxis_title = 'No of edits',
                                                    xaxis_title = 'Date_time_information',
                                                    height=1000, 
                                                    )}
    
    except Exception as e:
        with open('errors.txt','a') as f:
            f.write(str(e))
            f.write('\n')


if __name__ == '__main__':    
    app.run_server(debug=True)

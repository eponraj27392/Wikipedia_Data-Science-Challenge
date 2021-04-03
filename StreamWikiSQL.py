# -*- coding: utf-8 -*-


import time
import pandas as pd
import numpy as np
from collections import deque
import datetime
import json
import sqlite3
import argparse

from sseclient import SSEClient as EventSource
from preprocess import Preprocessing_mod
from dash.dependencies import Output, Input


conn = sqlite3.connect('WikiEventStream.db')
c    = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS WikiEventStreams(id, title, comment, user, server_url, wiki, meta_dt,  length_old, length_new)")
        conn.commit()
        
    except Exception:
        print('Error Occurs in creating Table...')
        
create_table()


def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


class WikiEventStreamer:
    def __init__(self, run_time = 5, url = None):
        self.url = url
        self.run_time = run_time
        
    
    def stream_wiki_data(self):
        start = time.time()
        for edit, event in enumerate(EventSource(self.url)):
            try:
                if event.event == 'message':
                    try:
                        json_data = json.loads(event.data) 
                    except ValueError:
                        pass
                    else: 
                      if json_data['type'] == 'edit':
                        updated_json_data  = flatten_dict(json_data) 
                        c.execute('''INSERT INTO WikiEventStreams (id, title, comment, user, server_url, wiki, meta_dt, length_old, length_new) 
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                  (updated_json_data['id'], updated_json_data['title'],updated_json_data['comment'],updated_json_data['user'], 
                                   updated_json_data['server_url'],updated_json_data['wiki'],updated_json_data['meta_dt'], updated_json_data['length_old'], updated_json_data['length_new'],))
                        conn.commit()
            
            except KeyError:
                print('Error during streaming ---')
            
            current_time_mins = round((time.time() - start)/(self.run_time*60), 2) if self.run_time is not None else round((time.time() - start)/(1*60), 2)
            
            if edit % 1000 ==0:
                print(current_time_mins)
            
            if self.run_time is not None:
                if current_time_mins > self.run_time:
                    print(f'=========={self.run_time} approached==========')
                    break
            
        return



                             

if __name__  == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default = 'https://stream.wikimedia.org/v2/stream/recentchange', type=str, help = 'url_to_stream_the_data')
    parser.add_argument('--run_time', default = None, type = int, help = 'time_to_stream_the API (minutes)')
    args = parser.parse_args()

    # Call the class
    streamer_class  = WikiEventStreamer(url = args.url, run_time = args.run_time)
    try:
        streamer_class.stream_wiki_data()
    except Exception:
        print('Error before streaming')      




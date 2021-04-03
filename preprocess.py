# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 20:39:36 2021

@author: jesakke
"""


import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyarrow.parquet as pq
import seaborn as sns
import re
from datetime import datetime
from utils import *

from collections import Counter



class Preprocessing_mod:
  def __init__(self, df, df_country = None):
    self.df         = df
    self.df_country = df_country 

  def Datetime_preprocess(self, df):
    df['meta_dt']                    = pd.to_datetime(df['meta_dt'])
    df[['hour', 'minute', 'second']] = pd.DataFrame([(i.hour, i.minute, i.second) for i in df['meta_dt']])
    df['hour_minute']                = df['meta_dt'].apply(lambda x: str(x.hour) + '_' +  '0' + str(x.minute) if len(str(x.minute)) <= 1 else str(x.hour) + '_' + str(x.minute))
    #df['utc_converted']              = df['timestamp'].apply(lambda x : datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    # print('DataFrame start Date_Time = ', df['meta_dt'].min())
    # print('DataFrame End Date_Time = ', df['meta_dt'].max())
    return df

  def Language_preprocess(self, df):
    df['language'] = df['wiki'].apply(lambda x : x.split('wiki')[0])
    df['language'] = df['language'].apply(lambda x : 'wikidata' if len(x) ==0 else x)
    df.loc[df[df.language == 'dewiktionary'].index.values, 'language'] = 'de'
    return df

  def LengthDiff_preprocess(self, df):
    df['length_diff']   = abs(df['length_old'] - df['length_new'])
    #df['revision_diff'] = abs(df['revision_old']  - df['revision_new'])
    return df

  def LengthComments_preprocess(self, df):
    df['length_comment'] = df['comment'].apply(lambda x : len(x))
    return df  

  def preprocess_country(self, df , df_country):
    df ['country'] = -1
    for i, df_subset in df.iterrows():
      try:
        df.loc[i, 'country'] = df_country[df_country.Code == df_subset.language]['Country'].values[0].strip()
      except:
        df.loc[i, 'country'] = 'NaN'
    return df 

  def meta_dt_X_axis(self, df):
      df['Date_hour_min'] =    df['meta_dt'].apply(lambda x : x.strftime("%Y-%m-%d %H:%M"))
      return df

  
  def _plot_all_languages(self, df):     
      df_all_languages         = df['Date_hour_min'].value_counts().sort_index().reset_index()
      df_all_languages.columns = ['Date_hour_min', 'all_lang_qty']
      return df_all_languages

      
  def _plot_de_languages(self, df):     
      df_de_languages         = df[df['language'] == 'de']['Date_hour_min'].value_counts().sort_index().reset_index()
      df_de_languages.columns = ['Date_hour_min', 'de_lang_qty']
      return df_de_languages
  
    
  def rol_avg_lenDiff(self, df,  win= 2):
      hour_minute_deutsch_lenDiff                         = df[df['language'] == 'de'].groupby('Date_hour_min').agg('length_diff').sum().reset_index()
      hour_minute_deutsch_lenDiff['DE_rolling_avg_len_diff'] = round(hour_minute_deutsch_lenDiff['length_diff'].rolling(window= win).mean())
      return hour_minute_deutsch_lenDiff
    
  

  def main_func(self):
    df               = self.Datetime_preprocess(self.df)
    df               = self.Language_preprocess(df)
    df               = self.LengthDiff_preprocess(df)
    df               = self.LengthComments_preprocess(df)
    df               = self.meta_dt_X_axis(df)
    df_all_languages = self._plot_all_languages(df)
    df_de_languages  = self._plot_de_languages(df)
    df_de_rollAvg    = self.rol_avg_lenDiff(df, win = round(df_de_languages.shape[0]/10))
    df1              = df_all_languages.merge(df_de_languages, left_on='Date_hour_min', right_on='Date_hour_min')
    df_final         = df1.merge(df_de_rollAvg, left_on='Date_hour_min', right_on='Date_hour_min')

    return df, df_final


    
   


# if __name__ == '__main__':
    
#     FILE_PATH         = 'C:\\Users\\jesakke\\Desktop\\exetta'
#     FILE_NAME         = '20210121_181328_recentchange_part1.parquet'
#     FILE_NAME_COUNTRY = 'Book1.xlsx'
    
    
    
#     df = pd.read_parquet(FILE_PATH + '/' + FILE_NAME, engine='pyarrow').reset_index(drop= True)
#     print('df_shape:', df.shape)
#     fixed_cols = df.columns.tolist()
#     df_country = None
    
    
#     call_cls  = Preprocessing_mod(df, df_country)
#     df, df_final      = call_cls.main_func()
#     #postfix_name    = '.csv'
#     #df_plot.to_csv(str(INPUT_DIR) +  "\\df_plot" + postfix_name, sep=';', decimal=',',  index=False)
    
#     #df_german = df[df.language == 'de'].reset_index(drop= True)
    

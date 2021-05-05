# Wikipedia_Data-Science-Exploration


Install all the necessary libraries using

```sh
pip install -r requirements.txt
```

if you encounter problems you may have to update pip first

```sh
python -m pip install --upgrade pip

```

## Preprocessing


A simple preprocessing class is created to read data from the ``database (sqlite3 - lightweight disk-based database)`` as ``pandas DF (data frame)``

Preprocessing class contains some methods which helps us to form a clean DF, which can be used further for Data Visualization.

It ``outputs 2 DF``, which can be used further for plotting desired metrics

Refer,  **preprocess.py**


## Exploratory Data Analysis

A comprehensive Exploratory Data Analysis for the Wikepedia Stream data with tidy ``python`` using a nice visualization library ``plotly``.

For this analysis, I have downloaded as json from Wiki API and converted to csv. (Just a sample data for understanding)

The data contains ``73565 rows & 38 columns`` of wikipedia API stream data ``between 17:11 till 18: 13 on Jan 21, 2021``. 

I explored **13 important topics** which will be the starting point in understanding the dataset

Refer to  **Wikipedia_EDA.ipynb**


*Note* :

Since I have used Google Colab for my analysis, if you are using Jupyter Notebook, kindly change the file path parameters.


## Streaming Live Data from API

To stream the wiki edit data using an API, I used SQLite3 to stream all the data into a data base.

For more information about SQLite3, refer [SQLite3](https://docs.python.org/3/library/sqlite3.html)

I have connected to SQLite DB and stored all json formatted API data in to SQL DB Table ```(DB = WikiEventStream.db ; TableName = WikiEventStreams)```

Two parameters involved to run the script ``StreamWikiSQL.py` 

1) url        = from which API-url we run  streams. [Default](https://stream.wikimedia.org/v2/stream/recentchange)

2) run_time  = How much time in minutes to run the Live stream & store our data in SQLite3 DB 
   
   (run_time  = None (No end time ; Default) 
                or run_time =  5, any int value represent minutes)
  
 
```sh
python -m StreamWikiSQL
```   
  
To change any parameters run..

```sh
python -m StreamWikiSQL --url https://stream.wikimedia.org/v2/stream/recentchange -- run_time 5
```

## Web App using DASH

Personally I prefer plotly visualization tool for all my Data Analysis (or Data Story telling). 

So I use Dash, from plotly, which helps us to develop web-based data visualization interfaces by putting together Plotly, React, and Flask.

For more information refer to [Dash](https://plotly.com/dash/)

For this analysis I made a simple web app, 

   * which connect the WikiEventStream.db (SQLite3 DB) --> preprocess the data --> plot a simple line graph dynamically (either stored data or live data)
   * The line graph will gets updated every 15 minutes of data with a desired time resolution is every minute.
   * For this challenge I have plotted dynamically Global Wikipedia language Edits per minute graph direcly from API.
   * To use a different metrics just tweek the parameters inside the file, **app.py**
 
Run the below code in console,

```sh
python -m app
```   

**Pipeline/Architecture**


![DashAppServer](https://github.com/eponraj27392/Wikipedia_Data-Science-Challenge/blob/main/pipeline.PNG)





**Run Dash App**


![DashAppServer](https://github.com/eponraj27392/Wikipedia_Data-Science-Challenge/blob/main/dash.PNG)




**Dash App plot Results**

```sh
Consider this as a starting point for app/dashboard dev, I plotted, global languages edit occur in Wikipedia every minute.
``` 

![DynamicPlottingImage](https://github.com/eponraj27392/Wikipedia_Data-Science-Challenge/blob/main/editspermin.PNG)




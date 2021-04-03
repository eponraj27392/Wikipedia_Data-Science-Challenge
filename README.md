# Wikipedia_Data-Science-Challenge


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

Preprocessing class contains some methos which helps us to form a clean DF, which can be used further for Data Visualization.

It ``outputs 2 DF``, which can be used further for plotting desired metrics

Refer,  **preprocess.py**



## Streaming Live Data from API

As the challenge required to stream the wiki edit data using an API, I used SQLite3 to stream all the data into a data base.

For more information about SQLite3, refer [SQLite3](https://docs.python.org/3/library/sqlite3.html)

I have connected to SQLite DB and stored all json formatted API data in to SQL DB Table ```(DB = WikiEventStream.db ; TableName = WikiEventStreams)```

Two parameters involved to run the script ``StreamWikiSQL.py` 

1) url        = from which API-url we run  streams. [Default](https://stream.wikimedia.org/v2/stream/recentchange)

2) run_time  = How much time in minutes to run the Live stream & store our data in SQLite3 DB 
   
   (run_time  = None (No end time ; Default) 
    run_time =  5, any int value represent minutes)
  
  
```sh
python -m StreamWikiSQL
```   
  
To change any parameters run..

```sh
python -m StreamWikiSQL --url https://stream.wikimedia.org/v2/stream/recentchange -- run_time 5
```



The proprocessing steps include 
[Preprocessing](preprocessing_wzl/README.md)

for further information on configuring the preprocessing pipeline.


**Preprocessing SFTP file (Data from Workshop)**

To create a *.csv file from SFTP xlsm file you need to copy the file into the folder ``data/SFTP/``
Then you can run the script

```sh
python -m scripts.preprocess_sftp
```

The timestep is set to 4ms. SOC, battery_id, engine_type, engine_type_id und engine_capacity are currently set to ``nan``. If data is available the script needs to be updated. 

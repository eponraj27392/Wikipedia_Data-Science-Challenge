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


A simple preprocess class is created to read the data as pandas df and ``output 2 DF's``

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

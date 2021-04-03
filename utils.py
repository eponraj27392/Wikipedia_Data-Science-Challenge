# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:45:37 2021

@author: jesakke
"""



from pathlib import Path
import logging
import matplotlib
import numpy as np
import random



# Global seeds
random.seed(42)
np.random.seed(42)


# Folders
PROJECT_DIR = Path.cwd()
INPUT_DIR   = PROJECT_DIR / "input_csv"
DB_SAVED    = PROJECT_DIR / 'WikiEventStream.db'



# OUTPUT_DIR = PROJECT_DIR / 'output'
# DEPLOYMENT_DIR = PROJECT_DIR / 'deployment'
# TESTS_OUTPUT_DIR = TESTS_DIR / 'output'
# FEATURE_CONFIG_DIR = PROJECT_DIR / 'preprocessing_wzl' / 'configs'
# POST_PROCESSING    = PROJECT_DIR / 'postprocessing'
# STACKING_POST_PROCESSING = OUTPUT_DIR / 'stacking'
# Path.mkdir(OUTPUT_DIR, exist_ok=True, parents=True)
# Path.mkdir(TESTS_OUTPUT_DIR, exist_ok=True, parents=True)
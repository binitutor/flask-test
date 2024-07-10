import os
from file_paths import config_path
import json

try:
    with open(config_path() + "config.json", "r") as fl:
        config_var = json.load(fl)
        print('Fetched credentials from config json file...')
except Exception as e:
    print('ERROR: Unable to fetched credentials from config json file...')
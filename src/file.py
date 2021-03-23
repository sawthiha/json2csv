import re
import json
import pandas as pd
import os
from os.path import join, isfile

import src.constants as constants

def listfiles(dir_path):
    return [
        file 
        for file in map(lambda fp: join(dir_path, fp), os.listdir(dir_path))
        if isfile(file)
    ]

def repath_csv(file_path):
    return join(constants.OUTPUT_DIR, re.sub(constants.FILE_EXTENSION_REGEX, r'.csv', re.search(constants.FILENAME_REGEX, file_path)[0], count = 1))

def read_json(file_path):
    return json.load(fp = open(file=file_path))

def to_csv(jsons, output_path):
    return pd.DataFrame(data = jsons).to_csv(output_path)

def jsons_to_csv(file_path):
    return to_csv(read_json(file_path), repath_csv(file_path))

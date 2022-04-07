from asyncio.windows_events import NULL
import csv, json, os
from numpy import empty
import pandas as pd
from flask import jsonify




def get_specific_parts(json_File_Path, get_item):
    parts = json.load(open(json_File_Path))

    if len(get_item) > 5:
        return "request too big"

    parts = {key: parts[key] for key in parts.keys()
                                & get_item}
    return parts

def get_sorted_by_hind(json_File_Path, get_item):
    parts = json.load(open(json_File_Path))

    if len(get_item) > 5:
        return "request too big"

    parts = {key: parts[key] for key in parts.keys()
                                & get_item}
    
    def extract_hind(json):
        try:
            return int(json['10']['hind'])
        except KeyError:
            return 0

    parts.sort(key=extract_hind(parts), reverse=True)

    return parts

def extract_hind(json):
        try:
            # Also convert to int since update_time will be string.  When comparing
            # strings, "10" is smaller than "2".
            return float(json['10']['hind'])
        except KeyError:
            return 0

def convert_csv_to_json(csv_file_path,json_file_path):
    print("csv to json conversion in progress...")

    df = pd.read_csv(csv_file_path, names=("Id","Serial","Nimi", "L1", "L2", "L3", "L4", "L5", "Sus1", "Sus2", "Tootja", "Hind"), low_memory=False)
    df.fillna({"Id": 0, "Serial": "Teadmata", "Nimi": "Teadmata", "L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0, "Sus1": 0.0, "Sus2": 0.0, "Tootja": "Teadmata", "Hind": 0.0}, inplace = True)
    df.astype({"Id": int, "Serial": str, "Nimi": str, "L1": int, "L2": int, "L3": int, "L4": int, "L5": int, "Sus1": float, "Sus2": float, "Tootja": str, "Hind": float})

    with open(json_file_path, 'w') as f:
        json.dump(df.to_dict(orient='records'), f, indent=4)
    print("Conversion finished.")

csv_file_path = r'data/LE.csv'
json_file_path = r'data/Le.json'
get_item = {'1', '10'}
convert_csv_to_json(csv_file_path,json_file_path)
#print(get_specific_parts(json_file_path, get_item))
#print(extract_hind(get_specific_parts(json_file_path,get_item)))
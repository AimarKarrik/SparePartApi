# app.py
# To start the api put this into the console: py -m flask run

from flask import Flask, request, jsonify
import json, csv, os, pandas


app = Flask(__name__)


def convert_csv_to_json(csv_file_path,json_file_path):
    print("csv to json conversion in progress...")

    df = pandas.read_csv(csv_file_path, names=("Id","Serial","Nimi", "L1", "L2", "L3", "L4", "L5", "Sus1", "Sus2", "Tootja", "Hind"), low_memory=False)
    df.fillna({"Id": 0, "Serial": "Teadmata", "Nimi": "Teadmata", "L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0, "Sus1": 0.0, "Sus2": 0.0, "Tootja": "Teadmata", "Hind": 0.0}, inplace = True)
    df.astype({"Id": int, "Serial": str, "Nimi": str, "L1": int, "L2": int, "L3": int, "L4": int, "L5": int, "Sus1": float, "Sus2": float, "Tootja": str, "Hind": float})

    with open(json_file_path, 'w') as f:
        json.dump(df.to_dict(orient='records'), f, indent=4)
    print("Conversion finished.")

csv_file_path = r'data/LE.csv'
json_file_path = r'data/Le.json'
convert_csv_to_json(csv_file_path, json_file_path)



@app.get("/parts")
def get_parts():
    parts = json.load(open(json_file_path))
    return str(parts)

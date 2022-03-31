print("API starting...")

# app.py
from flask import Flask, request, jsonify
import json
import csv
import os

app = Flask(__name__)


def make_parts():
    csvFilePath = r'data/DemoData.csv'
    jsonFilePath = r'data/demoData.json'

    if (os.path.exists('data/demoData.json') == True):
        os.remove('data/demoData.json')

    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['Id']
            data[key] = rows
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    PartsData = open('data/demoData.json')
    PartsData = json.load(PartsData)
    return PartsData



parts = make_parts()




@app.get("/parts")
def get_parts():
    return parts

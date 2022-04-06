print("API starting...")

# app.py
# To start the api put this into the console: python -m flask run

from flask import Flask, request, jsonify
import json
import csv
import os

app = Flask(__name__)


def make_parts():
    csvFilePath = r'data/LE.csv'
    jsonFilePath = r'data/Le.json'

    if (os.path.exists('data/Le.json') == True):
        os.remove('data/Le.json')

    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        print("Conversion CSV to JSON in progress")
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

    print("Conversion finished")
    PartsData = open('data/Le.json')
    PartsData = json.load(PartsData)
    return PartsData



parts = make_parts()




@app.get("/parts")
def get_parts():
    return parts

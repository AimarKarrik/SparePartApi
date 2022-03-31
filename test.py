import json
import csv
import os


    #LE.csv on liiga suuur et funkeda pls leia tee kuidas hakkida
def make_json():
    csvFilePath = r'data/DemoData.csv'
    jsonFilePath = r'data/DemoData.json'

    if (os.path.exists('data/demoData.json') == True):
        os.remove('data/DemoData.json')

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

    #PartsData = open('data/demoData.json')
    #PartsData = json.load(PartsData)
    #return PartsData

print(make_json())
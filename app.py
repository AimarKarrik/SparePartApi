# app.py
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json, csv, os, pandas



app = Flask(__name__)
api = Api(app)

def get_csv_convert_to_dict(csv_file_path,):
    print("csv to json conversion in progress...")


    df = pandas.read_csv(csv_file_path, names=("Id","Serial","Nimi", "L1", "L2", "L3", "L4", "L5", "Sus1", "Sus2", "Tootja", "Hind"), low_memory=False)
    df.fillna({"Id": 0, "Serial": "Teadmata", "Nimi": "Teadmata", "L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0, "Sus1": 0.0, "Sus2": 0.0, "Tootja": "Teadmata", "Hind": 0.0}, inplace = True)
    df.astype({"Id": int, "Serial": str, "Nimi": str, "L1": int, "L2": int, "L3": int, "L4": int, "L5": int, "Sus1": float, "Sus2": float, "Tootja": str, "Hind": float})

    print("Conversion finished.")
    return df.to_dict(orient='records')

csv_file_path = r'data/LE.csv'


class get_part_by_id(Resource):
    def get(self, property, decending):
        
        all_parts = get_csv_convert_to_dict(csv_file_path)

        sorted_parts = sorted(all_parts, key=lambda d: d[property], reverse=decending)
        return sorted_parts, 200

api.add_resource(get_part_by_id, '/sortby/<string:property>/<bool:decending>')



if __name__ == '__main__':
    app.run(debug=True)




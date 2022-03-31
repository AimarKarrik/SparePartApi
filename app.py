print("API starting...")

# app.py
from flask import Flask, request, jsonify
import pandas

app = Flask(__name__)

parts = pandas.read_json(r"data/DemoData.json")

@app.get("/parts")
def get_parts():
    return parts

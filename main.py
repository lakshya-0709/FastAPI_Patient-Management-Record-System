from fastapi import FastAPI
import json

app=FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {'message':'Patient Management Record System API'}

@app.get('/about')
def about():
    return {'message': 'Functional API to manage patient records'}

@app.get('/display')
def display():
    data = load_data()
    return data


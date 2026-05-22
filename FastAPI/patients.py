import json
from fastapi import FastAPI

app = FastAPI()

# Load JSON data
def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def home():
    return {"message": "Patient API"}

@app.get("/view")
def view():
    data = load_data()
    return data
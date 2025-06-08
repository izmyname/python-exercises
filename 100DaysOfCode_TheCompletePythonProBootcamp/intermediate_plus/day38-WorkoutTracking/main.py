import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


ask_user = input("what exercise did you do today? ")

def nutrionix(user_input):
    
    endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"
    header = {
        "Content-Type": "application/json",
        "x-app-id": os.environ["APP_ID"],
        "x-app-key": os.environ["API_KEY"]
    }
    parameters = {
        "query": user_input,
        "weight_kg": 80,
        "height_cm": 190,
        "age": 30
    }
    response = requests.post(url=endpoint, json=parameters, headers=header)
    response.raise_for_status()
    return response.json()['exercises'][0]

nutrionix_data = nutrionix(ask_user)

def sheety(data):
    
    endpoint = "https://api.sheety.co/8313f14cee8168abbaa9281781a41c73/day38Workout/workouts"
    header = {
        "Authorization": f"Bearer {os.environ['SHEETY_BEARER']}"
    }
    data= {
        "workout":{
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": data['name'].title(),
            "duration": round(data['duration_min']),
            "calories": data['nf_calories']
        }
    }
    
    response = requests.post(url=endpoint, json=data, headers=header)
    response.raise_for_status()
    return response.json()

sheety(nutrionix_data)
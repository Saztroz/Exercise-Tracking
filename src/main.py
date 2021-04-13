import requests
from datetime import datetime
import os

GENDER = "MALE"
WEIGHT_KG = 91
HEIGHT_CM = 188
AGE = 32

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

sheety_endpoint = os.environ.get("sheety_endpoint")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell me which exercises you did: ")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
    sheety_response = requests.post(
            sheety_endpoint, 
            json=sheet_inputs, 
            headers=bearer_headers
    )

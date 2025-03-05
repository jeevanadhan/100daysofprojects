import requests
from datetime import datetime
import os
APP_ID=os.environ.get("APP_ID")
APP_KEY=os.environ.get("APP_KEY")
NUTRITIONIX_ENDPOINT=os.environ.get("NUTRITIONIX_ENDPOINT")
SHEETY_ENDPOINT=os.environ.get("SHEETY_ENDPOINT")
my_params={
    "query":input("tell me which exercise you did: ")
}
header={
    'x-app-id':APP_ID,
    'x-app-key':APP_KEY
}
formatted_date=datetime.now().strftime("%y/%d/%m")
formatted_time=datetime.now().strftime("%H,%M,%S")

response=requests.post(url=NUTRITIONIX_ENDPOINT,json=my_params,headers=header)
response.raise_for_status()
data=response.json()
if "exercises" in data and len(data["exercises"]) >0:
    exercise_name=data["exercises"][0]["name"]
    duration=data["exercises"][0]["duration_min"]
    calories=data["exercises"][0]["nf_calories"]

else:
    print("no exercise data found")
    exit()
workout_params={
    "sheet1":{
        "date":formatted_date,
        "time":formatted_time,
        "exercise":exercise_name,
        "duration":duration,
        "calories":calories
    }
}
token=os.environ.get("BEARER_TOKEN")
header1={
    "Authorization":f"Bearer {token}"
}
sheety_response=requests.post(url=SHEETY_ENDPOINT,json=workout_params,headers=header1)
print("Sheety API Response:", sheety_response.text)

sheety_response.raise_for_status()

print(sheety_response.text)
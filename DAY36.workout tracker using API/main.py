import requests
from datetime import datetime
import os
APP_ID="9acdae3a"
APP_KEY="72ef75be67278af52970399dffe33ed2"
NUTRITIONIX_ENDPOINT='https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT="https://api.sheety.co/0878ff3d6090c64de5156589cb31c2db/workoutSheet/workouts"
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
print(data)
if "exercises" in data and len(data["exercises"]) >0:
    exercise_name=data["exercises"][0]["name"]
    duration=data["exercises"][0]["duration_min"]
    calories=data["exercises"][0]["nf_calories"]

else:
    print("no exercise data found")
    exit()
workout_params={
    "workout":{
        "Date":formatted_date,
        "Time":formatted_time,
        "Exercise":exercise_name,
        "Duration":duration,
        "Calories":calories
    }
}
token=os.environ.get('BEARER_TOKEN')
header1={
    "Authorization":f"Bearer dmfkdjfjakdnffkljadflkndjfnaksdfndjdnfjksadndfnadkjfdasdjfaA"
}

sheety_response=requests.post(url=SHEETY_ENDPOINT,json=workout_params,headers=header1)
print("Sheety API Response:", sheety_response.text)

sheety_response.raise_for_status()

print(sheety_response.text)
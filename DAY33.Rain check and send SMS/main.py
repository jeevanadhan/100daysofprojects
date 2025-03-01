import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")
weather_api_key = os.getenv("WEATHER_API_KEY")

if not account_sid or not auth_token or not weather_api_key:
    raise ValueError("Missing required environment variables. Please set ACC_SID, AUTH_TOKEN, and WEATHER_API_KEY.")

params = {
    "lat": 13.082680,
    "lon": 80.270721,
    "appid": weather_api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
json_data = response.json()

weather_id = [forecast["weather"][0]["id"] for forecast in json_data["list"]]

if any(main_id < 700 for main_id in weather_id):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12525126207',
        to='+919361963057',
        body="It's going to rain, so take an umbrella!"
    )
    print(f"Message status: {message.status}")
else:
    print("No rain expected.")

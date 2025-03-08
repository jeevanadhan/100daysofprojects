#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import flight_data
from flight_data import FlightData
from flight_search import FlightSearch
import os
SHEETY_ENDPOINT=os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN=os.environ.get("SHEETY_TOKEN")
flight=FlightSearch()
flightdata=FlightData()
header={
    "Authorization":f"Bearer {SHEETY_TOKEN}"
}
response=requests.get(url=SHEETY_ENDPOINT,headers=header)
data=response.text
print(data)
print(response.json())
print(flightdata.get_city_names_only(data=data))
# result=flight.flight_prize_finder(original_location,destination_location)
#
# # Check if result is returned
# if result:
#     print(result)
# else:
#     print("No flight data found or an error occurred.")

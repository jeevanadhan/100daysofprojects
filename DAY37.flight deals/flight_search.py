import requests
import datetime
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.date=datetime.datetime.now().strftime("%y-%m-%d")
        self.FLIGHT_SEARCH_ENDPOINT= "https://test.api.amadeus.com/v2/shopping/flight-offers"
    def flight_prize_finder(self,origin_location,destination_location):
        my_params={
            "originLocationCode":origin_location,
            "destinationLocationCode":destination_location,
            "departureDate":self.date,
            "adults":1
        }
        response=requests.get(url=self.FLIGHT_SEARCH_ENDPOINT,params=my_params)
        data=response.json()
        return data



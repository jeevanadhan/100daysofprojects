
import requests,os
import datetime
from amadeus import Client,ResponseError,Location
from currency_converter import CurrencyConverter
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.date=datetime.datetime.now().strftime("%Y-%m-%d")
        self.API_KEY=os.environ.get('API_ID')
        self.API_SECRET=os.environ.get("API_SECRET")
        self.amadeus = Client(client_id=self.API_KEY, client_secret=self.API_SECRET)
        self.c=CurrencyConverter()
    def flight_prize_finder(self,origin_location,destination_location):
        try:
            response = self.amadeus.shopping.flight_offers_search.get(originLocationCode=origin_location,
                                                                      destinationLocationCode=destination_location,
                                                                      departureDate=self.date,
                                                                      adults=1)
            data=response.data
            if data:
                for data in data:
                    price=data["price"]["grandTotal"]
                    inr_amount = self.c.convert(price, "EUR", "INR")
                    return f"{inr_amount:.2f}"
            else:
                return "no data"

        except ResponseError as e:
            print(f"Error fetching flight data: {e}")
            return None

import os
import requests
from dotenv import load_dotenv

load_dotenv()



class FlightSearch:
    def __init__(self):
        self.url = "https://test.api.amadeus.com/v1/"
        self.get_flights_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.api_key = os.environ["AMADEUS_KEY"]
        self.api_secret= os.environ["AMADEUS_SECRET"]
        self.token = self.get_token()
        
    def get_token(self):
        endpoint = f"{self.url}/security/oauth2/token"
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        response = requests.post(url=endpoint, data=data, headers=header)
        response.raise_for_status()
        return response.json()["access_token"]
    
    def get_iata_codes(self, city):
        endpoint = f"{self.url}/reference-data/locations/cities"
        header={
            "Authorization": f"Bearer {self.token}",
        }
        data = {
            "keyword": city,    
        }
        response = requests.get(url=endpoint, params=data, headers=header)
        response.raise_for_status()
        return response.json()["data"][0]["iataCode"]
    
    def get_flights(self, home ,dest,date_depart,date_return, cur):
        
        endpoint = self.get_flights_url
        header={
            "Authorization": f"Bearer {self.token}",
        }
        data = {
            "originLocationCode": home,
            "destinationLocationCode": dest,
            "departureDate": date_depart,
            "returnDate": date_return,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": cur,
            "max": 10,
        }
        
        response = requests.get(url=endpoint, params=data, headers=header)
        response.raise_for_status()
        return response.json()
    
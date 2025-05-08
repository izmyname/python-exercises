import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_FLIGHT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
            self._api_key = os.environ["AMADEUS_API_KEY"]
            self._api_secret = os.environ["AMADEUS_API_SECRET"]
            self._token = self._get_new_token()
        
    def iata_codes(self, city):

        headers = {"Authorization": f"Bearer {self._token}"}
            
        parameters = {
            "keyword": city.upper(),
            "include": "AIRPORTS"
        }
        
        airport = requests.get(url=AMADEUS_URL, params=parameters, headers=headers)
        airport = airport.json()
        
        try:
            airport_code = airport["data"][0]['iataCode']
        except ValueError:
            print("Something went wrong")
        except KeyError:
            print("No key found")
        
        return airport_code
        
    def _get_new_token(self):        
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body) 
        response = response.json()
        
        return response["access_token"]
    
    def check_flight(self, my_city, dest_city, dep_time, return_time):
        
        headers = {"Authorization": f"Bearer {self._token}"}
        
        flight_params = {
            "originLocationCode": my_city,
            "destinationLocationCode": dest_city,
            "departureDate": dep_time.strftime("%Y-%m-%d"),
            "returnDate":  return_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": True,
            "currencyCode": "GBP",
        }
            
        response = requests.get(url = AMADEUS_FLIGHT, params= flight_params, headers = headers)
        
        if  response.status_code != 200:
            print(f"Oops! Something went wrong. Status {response.status_code}")
            
        return response.json()
        
    
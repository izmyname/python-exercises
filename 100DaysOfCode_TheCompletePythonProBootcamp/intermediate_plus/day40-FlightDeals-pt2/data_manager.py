import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.bearer = os.environ["SHEETY_BEARER"]
        self.url = "https://api.sheety.co/8313f14cee8168abbaa9281781a41c73/day39FlightDeals/prices"
        self.users_endpoint = os.environ["SHEETY_USERS"]
        self.prices_endpoint = os.environ["SHEETY_PRICES"]
        
    def get_sheet(self):
        header = {
            "Authorization":f"Bearer {self.bearer}"
        }
        response = requests.get(url=self.url, headers=header)
        response.raise_for_status()
        return response.json()["prices"]
    
    def add_iataCodes(self, sheet):
        header = {
            "Authorization":f"Bearer {self.bearer}"
        }
        
        for entry in sheet:
            data = {
                "price": {
                    "iataCode": entry["iataCode"],
                },
            }
            
            response = requests.put(url=f"{self.url}/{entry['id']}", json=data, headers=header)
            response.raise_for_status()
            
        return response.json()
    
    def get_customer_emails(self):

        header = {
            "Authorization":f"Bearer {self.bearer}"
        }
        response = requests.get(url=self.users_endpoint, headers=header)
        response.raise_for_status()
        return response.json()['users']

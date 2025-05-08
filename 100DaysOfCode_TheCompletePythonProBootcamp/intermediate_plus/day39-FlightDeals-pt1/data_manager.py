import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEET ="https://api.sheety.co/8313f14cee8168abbaa9281781a41c73/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_url = SHEET
        self.name = os.environ["USERNAME"]
        self.password = os.environ["PASSWORD"]
        self.auth = HTTPBasicAuth(self.name, self.password)
        
    def fetch_data(self):
        response = requests.get(url=self.sheet_url, auth=self.auth)
        response.raise_for_status()
        response = response.json()["prices"]
                
        return response
    
    def put_data(self,sheet_data):
        
        for n in range(len(sheet_data)):
            sheet_id = sheet_data[n]["id"]
            sheety_put_endpoint= f"{SHEET}/{sheet_id}"
            input_iata = {
                
                "price":{
                    "iataCode": sheet_data[n]["iataCode"]
                }
                
            }
            update_sheet = requests.put(url=sheety_put_endpoint, json=input_iata, auth=self.auth)
            update_sheet.raise_for_status()
            
        return update_sheet
        
            

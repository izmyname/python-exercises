#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements
from data_manager import DataManager
from flight_search import FlightSearch
# from flight_data import FlightData
import datetime as dt

tomorrow_date = dt.datetime.now() + dt.timedelta(days=1)
six_months_date = dt.datetime.now() + dt.timedelta(days= 6*30)

data_manager = DataManager()
flight_search = FlightSearch()

MY_CITY = "LON" 

# screw you, shitty
sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': 'DBN', 'lowestPrice': 378, 'id': 10}]
# sheet_data = data_manager.fetch_data()

# for n in range(len(sheet_data)):
#     sheet_data_dict = sheet_data[n]
#     if sheet_data_dict["iataCode"] == "":
#         airport_code = flight_search.iata_codes(sheet_data_dict["city"])
#         sheet_data_dict["iataCode"] = airport_code
        
# data_manager.put_data(sheet_data)

for airport in sheet_data:
    dest_city = sheet_data[0]["iataCode"]
    flight_search.check_flight(MY_CITY, dest_city,tomorrow_date,six_months_date)
    


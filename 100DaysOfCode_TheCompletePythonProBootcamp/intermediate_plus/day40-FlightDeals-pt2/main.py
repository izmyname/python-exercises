import datetime
from time import sleep
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

ORIGIN = "LON"
CUR = "GBP"

DEPARTURE_DATE = (datetime.datetime.now()+ datetime.timedelta(days=1)).strftime("%Y-%m-%d")
RETURN_DATE = (datetime.datetime.now() + datetime.timedelta(6*30)).strftime("%Y-%m-%d")


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheet()

user_data = data_manager.get_customer_emails()
user_emails = []
for user in user_data:
    user_emails.append(user["what'sYourEmail?"])



for data in sheet_data:
    data["iataCode"] = flight_search.get_iata_codes(data["city"])

# data_manager.add_iataCodes(sheet_data)   

for entry in sheet_data:
    flights = flight_search.get_flights(ORIGIN, entry["iataCode"], DEPARTURE_DATE, RETURN_DATE, CUR)
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{entry['city']}: £{cheapest_flight.price}")
    notification_manager.notify(entry, cheapest_flight)
    notification_manager.send_emails(user_emails, entry, cheapest_flight)
    
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(ORIGIN, entry["iataCode"], DEPARTURE_DATE, RETURN_DATE, is_direct=False)
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")



    

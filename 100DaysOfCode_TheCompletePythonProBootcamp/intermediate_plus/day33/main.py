import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# print(f"{longitude}  {latitude}")

LATITUDE = -12.067580
LONGITUDE = -77.033794

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"sunrise: {sunrise}, sunset: {sunset}")
import requests
from twilio.rest import Client

api_key=""
account_sid = ""
auth_token = ""

parameters={
    "lat": 99.999,
    "lon": 66.666,
    "cnt": 4,
    "appid": api_key,
}

weather = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
weather.raise_for_status()
weather = weather.json()
weather_code = weather['cod']
weather_list = weather["list"]

rain = False 

for d in range(len(weather_list)):
    weather_id=weather_list[d]["weather"][0]["id"]
    if weather_id < 700:
        rain = True
        
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "Ta se ag cur baisti inniu",
        from_  = "+15000000",
        to = "+7000000"
        )
print(message.status)
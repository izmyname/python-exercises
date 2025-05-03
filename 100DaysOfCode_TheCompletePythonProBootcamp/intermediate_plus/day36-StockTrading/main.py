import requests
from twilio.rest import Client
import html

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stocks_api_key = ""
stocks_endpoint = "https://api.twelvedata.com/time_series"

stocks_params = {
    "symbol": STOCK,
    "interval": "1day",
    "format": "json",
    "type": "stock",
    "outputsize": 2,
    "apikey": stocks_api_key,
    
}

stock_price = requests.get(url=stocks_endpoint, params=stocks_params)
stock_price.raise_for_status()
stock_price = stock_price.json()
stock_price = stock_price["values"]

stock_price_close = [stock_price[n]["close"] for n in range(len(stock_price))]

stock_yesterday = float(stock_price_close[0])
stock_before_yesterday = float(stock_price_close[1])

percentage_difference = ((stock_yesterday - stock_before_yesterday)/stock_before_yesterday) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_api = ""
news_endpoint = "https://newsapi.org/v2/everything"

news_params = {
    "q": COMPANY_NAME,
    "apikey": news_api,
    "language": "en",
    "pageSize": 3,
}

news = requests.get(url=news_endpoint, params=news_params)
news.raise_for_status()
news = news.json()
news = news["articles"]

tesla_daily = []

for n in range(len(news)):
    news_title = html.unescape(news[n]["title"])
    news_description = html.unescape(news[n]["content"])
    
    tesla_news = {}
    tesla_news["title"]=news_title
    tesla_news["description"]=news_description
    tesla_daily.append(tesla_news)
    
    

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    
sid = ""
auth = ""
my_phone = ""
message = f"TSLA: 🔺{round((percentage_difference), 2)}%\nHeadline: {tesla_daily[0]["title"]}\nBrief: {tesla_daily[0]["description"]}\n\nHeadline: {tesla_daily[1]["title"]}\nBrief: {tesla_daily[1]["description"]}\n\nHeadline: {tesla_daily[2]["title"]}\nBrief: {tesla_daily[2]["description"]}"

# Send SMS
if percentage_difference < -5 or percentage_difference > 5:
    account_sid = sid
    auth_token = auth
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_ ='+15088127249',
        to = my_phone,
        body = message,
    )
    print(message.status)
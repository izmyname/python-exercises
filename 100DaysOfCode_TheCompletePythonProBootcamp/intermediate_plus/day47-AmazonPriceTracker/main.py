import smtplib
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# using requests to fetch the data from the site
URL="https://www.amazon.de/-/en/Diohauxi-Interchangeable-Figures-Chassis-Ornament/dp/B0DXPXPRGX/ref=sr_1_7?crid=MEAJLK290NQI&dib=eyJ2IjoiMSJ9.vIs0TiZDd0m468QuAYLqdY2NfYxQc6CYAFxsOjPvUWI-yNhmx-rjAqrRZ45srtjaadaooSAlKQbthw1WOAN7xs6i05l0uqwynX4qorVaPLdiAYoLYpwBICVbOfdVmODDIBV9ZD9IMn56XRSXPQ3Pjau5YP1BjIPmRQLmCC8mCE5lsW16pbzft9gZIWQQq9wpeiVwVX_xP9CSA3AiBVFwgyw53KLzbaOTS4EzV8dh9pYUP87ldgMsIRjZKK0X1276FzhfZ2s8yQxzcx0v5jcOigBT38eNVIMQwj3t9Eia0GY.odqf2Cgp7FY0FkZNkljHhYcmgQrH72t6OVKjKz_nwQ0&dib_tag=se&keywords=2b%2Bfigurine&qid=1747218436&sprefix=2b%2Bfigurine%2Caps%2C207&sr=8-7&th=1"
HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0",
    "Accept-Language": "en-US",
}

response = requests.get(url=URL, headers=HEADER)
website = response.text

# using Soup to fetch the specific data from the site
soup = BeautifulSoup(website, "html.parser")
price = float(soup.find(name="span", class_="aok-offscreen").getText().split("€")[1])
product_name = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText().strip()


# send an email if price is lesser, than $100
if price < 40:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=os.environ["SENDER"], password=os.environ["SENDER_PASSWD"])
        connection.sendmail(from_addr=os.environ["SENDER"], to_addrs=os.environ["RECEIVER"], msg=f"Subject:Amazon Price Alert\n\n{product_name} now costs {price} EUR")
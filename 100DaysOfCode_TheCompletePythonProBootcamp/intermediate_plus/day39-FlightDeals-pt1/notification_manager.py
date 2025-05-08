#Screw twilio
import smtplib
import os
from dotenv import load_dotenv

load_dotenv() 

class NotificationManager:
    def __init__(self):
        self.sender = os.environ["MY_MAIL"]
        self.passwd = os.environ["MY_PASS"]
        self.receiver = os.environ["RECEIVER"]
    
    
    def notify(self, sheet, flight):
        if float(flight.price) < float(sheet["lowestPrice"]):
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.sender, password=self.passwd)
                connection.sendmail(from_addr=self.sender, to_addrs=self.receiver, msg=f"Subject:Low Price Alert!\n\nOnly {flight.price} to fly from {flight.origin_airport} to {flight.destination_airport}, on {flight.out_date} until {flight.return_date}") 
        return
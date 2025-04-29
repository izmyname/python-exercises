import smtplib
import datetime as dt
import random

with open("quotes.txt" ,"r") as quotes:
    quotes_list = quotes.readlines()

quotes_list = [q.strip() for q in quotes_list]
random_quote = random.choice(quotes_list)

now = dt.datetime.now()
theday = now.weekday()

my_email = "???@gmail.com"
password = "???" 

connection = smtplib.SMTP("smtp.gmail.com", 666)
connection.starttls()
connection.login(user=my_email, password=password)

if theday == 1:
    
    connection.sendmail(from_addr=my_email, to_addrs="???@yahoo.com", msg=f"Subject: Your quote\n\n{random_quote}")
else:
    connection.sendmail(from_addr=my_email, to_addrs="???@yahoo.com", msg=f"Subject: Your quote\n\nnope")

connection.close()

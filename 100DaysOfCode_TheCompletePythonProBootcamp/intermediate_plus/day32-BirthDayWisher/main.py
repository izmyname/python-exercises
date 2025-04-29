import pandas as pd
import smtplib
import datetime as dt
import random
##################### Extra Hard Starting Project #####################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# login to my mail
my_email = "izmyname@gmail.com"
my_password = "12345 " 
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=my_password)

# import all files
birthday_templates = []
emails_dataframe = pd.read_csv("birthdays.csv") 

for n in range(1,4):
    with open(f"letter_templates/letter_{n}.txt") as n:
        n = n.read()
        birthday_templates.append(n)
        
# set variables for time and date
now = dt.datetime.now()
now_month =  now.month
now_day = now.day

# send mails 
for(index, row) in emails_dataframe.iterrows():
    if (now_month == row.month) and (now_day == row.day):
        chosen_template = random.choice(birthday_templates).replace("[NAME]", row["name"])
        connection.sendmail(from_addr=my_email, to_addrs=row.email, msg=f"Subject: Happy Birthday!\n\n{chosen_template}")

connection.close()

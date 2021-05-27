##################### Extra Hard Starting Project ######################

import smtplib
import pandas
import pandas as pd
from random import choice
import datetime as dt

EMAIL = "email@goeshere.com"
PASSWORD = "p455w0rd"

#save letters to vars
with open("letter_templates/letter_1.txt") as file:
    letter_1 = file.read()
with open("letter_templates/letter_2.txt") as file:
    letter_2 = file.read()
with open("letter_templates/letter_3.txt") as file:
    letter_3 = file.read()

letters =[letter_1, letter_2, letter_3]

#get current day
current_time = dt.datetime.now()
day = current_time.day
month = current_time.month

#get birthdays
file = pandas.read_csv("birthdays.csv")
print(file)

for index, row in file.iterrows():
    if row.month == month:
        if row.day == day:

            letter = choice(letters)

            letter = letter.replace("[NAME]",row["name"])
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(to_addrs=row.email, from_addr=EMAIL, msg=f"Subject:It's your birthday!\n\n{letter}")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





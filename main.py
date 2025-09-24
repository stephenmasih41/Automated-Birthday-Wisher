#Imports
import pandas as pd
import datetime as dt
import random
import smtplib

#Constants
birthday_people = []
my_email = "stephenmasih39@gmail.com"
password = "nzurmsojhgplympb"

#CSV File
people = pd.read_csv("birthdays.csv")

#Checking month and date as of today
today = dt.datetime.now()
today_month = today.month
today_day = today.day

# Comparing today's data with csv data
for _,person in people.iterrows():
    if person['month'] == today_month and person['day'] == today_day:
        # Converting the Data Frame to dictionary for easier usage
        birthday_people.append(person.to_dict())

#Only Assigning the variables if List is not empty
if birthday_people:
    for person in birthday_people:
        birthday_person = person["name"]
        person_email = person["email"]
else:
    #Using pass to show nothing
    pass

#Only using the random template and sending email if friend has a birthday today
if birthday_people:
    letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    #Using random template and changing name
    with open(letter_path) as file:
        data = file.read()
        # Changing the placeholder
        data = data.replace("[NAME]",birthday_person)
        # Sending Email
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person_email,
                msg=f"Subject:Happy Birthday\n\n{data}")



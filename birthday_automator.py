import random
import datetime as dt
import smtplib
import csv

today_date = dt.datetime.now()
today_month = today_date.month
today_day = today_date.day

my_email = "pratikjh1011@gmail.com"
password = "Testing@100"

with open("birthdays.csv", mode="r", newline="") as birth_data:
    data = csv.DictReader(birth_data)
    for row in data:
        name = row["name"]
        email = row["email"]
        month = int(row["month"])
        day = int(row["day"])

        if today_month == month and today_day == day:
            random_num = random.randint(1, 3)
            with open(f"letter_templates/letter_{random_num}.txt") as letter_file:
                letter = letter_file.read()
                letter = letter.replace("[NAME]", name)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=my_email,
                                    msg=f"Subject:Happy Birthday!\n\n{letter}")

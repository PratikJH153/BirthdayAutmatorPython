import datetime as dt
import smtplib
import random

my_email = "pratikjh1011@gmail.com"
password = "Testing@100"

today_date = dt.datetime.now()
week_day = today_date.weekday()

if week_day == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Motivational Boost on Monday!\n\n{random_quote}")


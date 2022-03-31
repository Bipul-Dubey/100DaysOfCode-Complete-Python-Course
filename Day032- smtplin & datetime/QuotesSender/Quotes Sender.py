import smtplib
import datetime as dt
import random

current=dt.datetime.now()
weekday=current.weekday()
# week day start from monday=0

sender_email="smtpcheck9@gmail.com"
sender_password="Smtp@1111"
receiver_email="raj12kumar21@yahoo.com"

if weekday==3:
    with open("quotes.txt") as quotes_file:
        all_quotes=quotes_file.readlines()
        quote=random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email,password=sender_password)
        connection.sendmail(from_addr=sender_email,to_addrs=receiver_email,
                            msg=f"Subject:Quotes\n\n{quote}")
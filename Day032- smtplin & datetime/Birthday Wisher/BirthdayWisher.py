import random
import smtplib
import pandas
import datetime as dt

sender_email=""
sender_password=""
receiver_email=""

today=dt.datetime.now()
today_tuple=(today.month,today.day)

data=pandas.read_csv("birthdays.csv")
birthday_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content=letter_file.read()
        content=content.replace("[NAME]",birthday_person["name"])

    # enter mail service provide in SMTP()
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:BirthdayWish\n\n{content}")

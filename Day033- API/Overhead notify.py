import time
import requests
import datetime as dt
import smtplib

MY_LAT=20.593683
MY_LNG=78.962883

sender_email=""
sender_password=""
receiver_email=""


def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()

    iss_latitude=float(data["iss_position"]["latitude"])
    iss_longitude=float(data["iss_position"]["longitude"])

    if MY_LAT-5<= iss_latitude <= MY_LAT+5 and MY_LNG-5<=iss_longitude<=MY_LNG+5:
        return True


def is_night():
    parameter={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
    response.raise_for_status()
    data=response.json()

    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now=dt.datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=sender_email,password=sender_password)
        connection.sendmail(from_addr=sender_email,to_addrs=receiver_email,
                            msg="Subject:LookUp ☝👆\n\nThe ISS is above you in the sky.")


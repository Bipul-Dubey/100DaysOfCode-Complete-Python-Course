import requests

end_point="https://api.openweathermap.org/data/2.5/onecall"
my_api_key=""
lat=0
lng=0
parameters={
    "lat":lat,
    "lon":lng,
    "exclude":"current,minutely,daily",
    "appid":my_api_key
}

response=requests.get(url=end_point,params=parameters)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]
weather=""
will_rain=False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    weather="Rainy Day"
else:
    weather="Sunny Day"
print(weather)

import smtplib

sender_email=""
sender_password=""
receiver_email=""

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=sender_email,password=sender_password)
connection.sendmail(from_addr=sender_email,to_addrs=receiver_email,msg=f"Subject:Weather Condition\n\n{weather}")
connection.close()

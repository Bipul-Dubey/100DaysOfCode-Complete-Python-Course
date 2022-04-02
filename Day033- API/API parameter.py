import requests
import datetime as dt

parameter={
    "lat":30.733315,
    "lng":76.779419,
    "formatted":0
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]


sunrise_hour=int(sunrise.split("T")[1].split(":")[0])
sunset_hour=int(sunset.split("T")[1].split(":")[0])

print(sunrise_hour,sunset_hour)
import requests
from datetime import datetime, time

MY_LAT=28.3949
My_LON=84.1240

parameters={
    "lat":MY_LAT,
    "lon":My_LON,
    "formatted":0
}
response=requests.get(url="https://api.sunrise-sunset.org/json")
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now=datetime.now()
print(time_now.hour)
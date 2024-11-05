import requests
import json

URL = "http://api.open-notify.org/iss-now.json"

Loc = requests.get(URL)
Loc = Loc.json()

lon= Loc["iss_position"]["longitude"]
lat= Loc["iss_position"]["latitude"]


print("CURRENT LOCATION OF THE ISS:")
print("Lon:" + str(lon))
print("Lat:" + str(lat))
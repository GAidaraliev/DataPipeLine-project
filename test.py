import urllib.request as req
import json
import requests
API_KEY = "a0bd5e5a4d9a4c4098f143006241003"
hours = 1
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris&hours={hours}"
# url = "https://moviesdatabase.p.rapidapi.com/titles/series/%7BseriesId%7D"
#
# headers = {
# 	"X-RapidAPI-Key": "52db4107d7msh20b314f03499073p17e21cjsn7cf283468464",
# 	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)
response = requests.get(url)
#
# session = req.urlopen(url)
# response = session.read().decode()
# data = json.loads(response)
# print(data)

#response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q=Paris&days={days}")
print(response.text)


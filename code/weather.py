import requests

api_key = "912b391751e19784d6353aab9a208e59"
city = input("Enter city: ")

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

response = requests.get(url)

data = response.json()

report = {"Temperature": (data["main"]["temp"]), "Weather": (data["weather"][0]["description"]), "Humidity": (data["main"]["humidity"])  }

for key, value in report.items():
    print(key, ":", value)


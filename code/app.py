from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = "Mihir"
    api_key = "912b391751e19784d6353aab9a208e59"
    city = "udaipur"
    if request.method == "POST":
        city = request.form["city"]

    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"
    data = requests.get(url).json()
    temperature = str(data["main"]["temp"]) + "°C"
    weather = data["weather"][0]["description"]
    return render_template("home.html", name=name, city=city, temperature=temperature, weather=weather)
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)

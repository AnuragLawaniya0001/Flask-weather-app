from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# You can get a free API key by signing up at https://openweathermap.org/api
API_KEY = "9a4dc41846bf44352b37b199a1978209xxxxxxx...."
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"


def get_weather_data(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_URL, params=params)
    return response.json()


def get_forecast_data(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(FORECAST_URL, params=params)
    return response.json()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    weather_data = get_weather_data(location)
    forecast_data = get_forecast_data(location)

    if weather_data.get('cod') != 200:
        return render_template('index.html', error="Location not found")

    return render_template('weather.html', weather=weather_data, forecast=forecast_data)


if __name__ == '__main__':
    app.run(debug=True)

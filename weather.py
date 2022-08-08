from flask import Flask
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key') 

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Home - No Data Available - Please Provide a City'

@app.route('/<place>')
def place(place):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{place}?unitGroup=metric&include=current&key={api_key}&contentType=json'
    response = requests.get(url)
    current = response.json()['days'][0]
    key_filter = {'datetime', 'temp', 'feelslike', 'humidity', 'windspeed', 'winddir', 'pressure', 'sunrise', 'sunset', 'description'}
    current = {key:current[key] for key in current.keys() & key_filter}
    return f'{current}'

if __name__ == '__main__':
    app.run(use_reloader=True)

import requests
from twilio.rest import Client

api_key = "fc3e5f445010425b77d20325493273c4"
api_url = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = "AC8f14d57b841f4b49aa57d382bd62b453"
auth_token = "6c1b597b42ec37c87ed708483666f0b0"

weather_params = {
    "lat": 41.450142,
    "lon": 2.247420,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_url, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hola Mama, ha de ploure, agafa un paraigues",
        from_="+15154747090",
        to="+34636641773"
    )

    print(message.status)

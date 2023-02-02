# Weather App
A Python script that uses the OpenWeatherMap API and Twilio API to check the weather forecast for the next 12 hours and send a text message if it will rain. 

## Requirements
- `requests` library for making API calls
- `twilio` library for sending text messages
- API keys for OpenWeatherMap and Twilio 

## How it works
1. Make a request to the OpenWeatherMap API for the weather forecast for the next 12 hours.
2. Check the condition codes for each hour in the forecast.
3. If the condition code indicates rain, create a text message using Twilio API.
4. Send the text message.

## Configuration
- Replace the placeholders in the script with your own API keys and Twilio phone numbers.
- Adjust the latitude and longitude values to your desired location.

## Usage
Run the script in your terminal or command prompt. If it's going to rain, you will receive a text message.

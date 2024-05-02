!pip install requests
import requests

city_name=input('Enter city name:')
API_key = '8d458d5b0dbb433e26e5af872fd9ef82'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
  print('Yes, We hit')
  data = response.json()
  print(data)

print('Weather is', data['weather'][0]['description'])
print('Current Temperature is', data['main']['temp'])
print('Feels like', data['main']['feels_like'])
print('Current Humidity is', data['main']['humidity'])

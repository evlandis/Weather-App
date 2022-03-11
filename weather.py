import requests

API_KEY = "" # This code needs an API key to work. For privacy reasons I cannot use the original key for this program as a public repo on GITHUB.
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name that you would like the weather for: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
#if valid, finds wanted weather info in the dictionary and prints it out to the user
if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperatureF = round((data["main"]["temp"] - 273.15) *(9/5) + 32,2) 
    temperatureC = round(data["main"]["temp"] - 273.15,2)
    humidity = data["main"]["humidity"]
    feelF = round((data["main"]["feels_like"]- 273.15) *(9/5) + 32,2)
    feelC = round((data["main"]["feels_like"]- 273.15),2)

    print("\nThe weather in the city", city, "is: ")
    print("Weather:", weather)
    print("Temperature:", temperatureF, "degrees Fahrenheit")
    print("Feels like: {} degrees Fahrenheit".format(feelF))
    print("Temperature:", temperatureC, "degrees Celsius")
    print("Feels like: {} degrees Celsius".format(feelC))
    print("Humidity is: {}%".format(humidity))
else:
    print("An error occured. ")
    

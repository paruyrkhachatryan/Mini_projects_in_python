
import requests

API_KEY = "db55f2e8b76adec5651cce58b6a66c08"


def get_city_name():
    return input("Enter a city name: ")


def get_weather_data(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()


def check_city_existence(city_name):
    data = get_weather_data(city_name)
    if data.get("cod") == "404":
        print("City not found. Please try again.")
        return False
    return data


def main():
    while True:
        city_name = get_city_name()
        weather_data = check_city_existence(city_name)
        if weather_data:
            print(weather_data)
            break


if __name__ == "__main__":
    main()

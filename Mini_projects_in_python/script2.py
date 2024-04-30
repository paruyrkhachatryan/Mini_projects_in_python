import requests

def get_city_name():
    """
    Requests the city name from the user.
    """
    return input("Enter a city name: ")


def get_weather_data(city_name, api_key):
    """
    Gets weather data for the specified city using OpenWeatherMap API.
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as error_n:
        print("Error:", error_n)
        return None


def check_city_existence(city_name, api_key):
    """
    Checks the existence of the specified city.
    """
    data = get_weather_data(city_name, api_key)
    if data and data.get("cod") == 404:
        print("City not found. Please try again.")
        return False
    return data


def display_weather_info(weather_data):
    """
    Displays weather information for the specified city.
    """
    if weather_data:
        city = weather_data.get("name")
        country = weather_data.get("sys", {}).get("country")
        weather = weather_data.get("weather", [])[0].get("description")
        temperature_kelvin = weather_data.get("main", {}).get("temp")
        temperature_celsius = temperature_kelvin - 273.15  # Convert Kelvin to Celsius
        humidity = weather_data.get("main", {}).get("humidity")
        wind_speed = weather_data.get("wind", {}).get("speed")
        
        print(f"Weather in {city}, {country}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature_celsius:.2f} °C") 
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")


def main():
    """
    Main function of the program.
    """
    api_key = "db55f2e8b76adec5651cce58b6a66c08"
    while True:
        city_name = get_city_name()
        weather_data = check_city_existence(city_name, api_key)
        if weather_data:
            display_weather_info(weather_data)
            break


if __name__ == "__main__":
    main()


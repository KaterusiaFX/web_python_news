# Сlient goes on worldweatheronline.com using API and returns data with weather info.

import requests


# I get API at worldweatheronline.com. It includes: key, q, format, num_of_days, lang
def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "1eab5659489b4e29ac5124654201405",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    # exception handling
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()  # this method raises an HTTPError if unsuccessful status code will appear.
        # json method returns request result in json format
        weather = result.json()
        # select from result only current_condition
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return weather["data"]["current_condition"][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False
    return False


if __name__ == "__main__":
    w = weather_by_city("Moscow,Russia")
    print(w)



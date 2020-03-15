from flask import current_app  # позволяет обращаться к текущему flask приложению
import requests


def weather_by_city(city_name):
    weather_url = current_app.config['WEARHER_URL']
    params = {
        "key": current_app.config['WEATHER_API_KEY'],
        "q": city_name,  # параметр q указывает на город
        "format": "json",  # ,будет выводится в формате json
        "num_of_days": 1,  # погода за 1 день
        "lang": "ru"  # на русском языке
    }

    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False


if __name__ == "__main__":
    weather = weather_by_city("Moscow,Russia")
    print(weather)



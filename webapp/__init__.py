# Создаю первый web-сервис

from flask import Flask, render_template  # импорт фрэймворка Flask, импорт модуля для работы с шаблонами
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city  # из файла weather.py (здесь просто weather) импортируем ф-ю weather_by_city

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
# Flask использует пути. Нужно привязать функ-ю - обработчик к какому-то пути на сайте
    @app.route('/')   # декоратор позволяет открывать ф-ю по url / (/ - это значит главная страница)
    def index():
        title = 'Новости Python'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = get_python_news()
        return render_template("index.html", page_title=title, weather=weather, news_list=news_list)

    return app



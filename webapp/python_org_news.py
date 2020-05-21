# client for collecting news from www.python.org
import requests

from datetime import datetime
from bs4 import BeautifulSoup

from webapp.db import db
from webapp.news.models import News


def get_html(url):  # get html page from https://www.python.org/blogs/.
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_python_news():  # choose <ul> with news, then choose only title, url, date and record it as a list of dicts.
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts')
        all_news = all_news.findAll('li')
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')  # strptime parsing string in Y-m_d format
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)
    return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()



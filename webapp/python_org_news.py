import requests

# библиотека берет на вход строку с html, преобразует в дерево элементов, среди которых
# можно делать поиск, добавлять, убавлять, получать контент.
# BeautifulSoup так же убирает часть огрехов html док-ов
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


# ф-я для создания дерева из html и для осущ-я поиска нужного эл-та
def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            result_news.append({
                "title": title,
                "url": url,
                "published": published

            })
        return result_news  # это будет список словарей, в каждом будет title, url, published
    return False

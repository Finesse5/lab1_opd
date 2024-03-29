import requests
from bs4 import BeautifulSoup
import time


import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = 'https://www.omgtu.ru/news/'


response = requests.get(url, verify=False)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')


    news_headings = soup.find_all('h3', class_='news-card__title')


    with open('news.txt', 'w', encoding='utf-8') as file:

        for heading in news_headings:

            file.write(heading.text.strip() + '\n')

            time.sleep(10)

    print("Список заголовков новостей успешно записан в файл 'omgtu_news_headings.txt'")
else:
    print("Ошибка при получении данных с сайта")

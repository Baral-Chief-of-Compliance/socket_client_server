import requests
import json
from bs4 import BeautifulSoup
from for_date import crate_str
import re


def get_timetable():
    url = "https://www.mstu.edu.ru/study/timetable/"

    response_get = requests.get(url)
    with open ("test.html", "w") as file:
        file.write(response_get.text)

    with open ("test.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    tag = soup.find(text=re.compile(f'{crate_str()}')).parent
    pers = tag.get('value')

    date = {
        "mode": 1,
        "pers": pers,
        "facs": 4,
        "courses": 4
    }
    response = requests.post(url, date)
    # if response.ok:
    with open ("test2.html", "w") as file:
        file.write(response.text)

    with open ("test2.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    tag = soup.find(text='ИВТб19о-1').parent

    href = url + tag.get("href")

    response_time_table = requests.get(href)

    with open ("time_table.html", "w") as file:
        file.write(response_time_table.text)
from __future__ import unicode_literals
from bs4 import BeautifulSoup
from requests import get
import youtube_dl


def user_input():
    name_video = input("Search for a song: ")
    print(f"Searching for \"{name_video}\"...")
    return name_video


def scrapping_youtube(name: str, amount: int):
    url = f"https://www.youtube.com/results?search_query={name}&sp=EgIQAQ%253D%253D"
    cookies = {"PREF": "f6=43418&f5=30&al=pt&f1=50000000"}

    response = get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("a", class_="yt-uix-tile-link", limit=amount)

    return titles


def filter_scrapping(titles: 'class'):
    names = []
    hrefs = []

    for title in titles:
        names.append(title.text)
        hrefs.append(title['href'])

    return names, hrefs


def display(names: list, hrefs: list):
    print()
    for index, name in enumerate(names):
        print(f"[{index + 1}] - {name}")

    number = int(input("Select a number: ")) - 1

    return hrefs[number]


def download(href: str):
    print()
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://www.youtube.com{href}"])


if __name__ == "__main__":
    download(display(*filter_scrapping(scrapping_youtube(user_input(), 5))))

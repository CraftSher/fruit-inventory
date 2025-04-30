import requests
from bs4 import BeautifulSoup

def get_football_news():
    url = "https://www.championat.com/football/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return "Не удалось получить данные с сайта."

        soup = BeautifulSoup(response.text, "html.parser")
        news_items = soup.find_all("a", class_="collection__item", limit=5)
        news = []

        for item in news_items:
            title_tag = item.find("span", class_="collection__item__content")
            if not title_tag:
                continue

            title = title_tag.text.strip()
            link = item.get("href")
            if link and not link.startswith("http"):
                link = "https://www.championat.com" + link

            news.append(f"{title}\n{link}")

        return "\n\n".join(news) if news else "Новостей не найдено."

    except Exception as e:
        return "Произошла ошибка при получении новостей."
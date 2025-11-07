import requests
from bs4 import BeautifulSoup

def parse_avito(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    ads = soup.select('div.iva-item-root-_lk9K')
    for ad in ads:
        title = ad.select_one('h3.styles-module-root-W_crH')
        price = ad.select_one('p[data-marker="item-price"]')
        link = ad.select_one('a[data-marker="item-title"]')

        print(
            f"Заголовок: {title.text.strip() if title else 'нет'}\n"
            f"Цена: {price.text.strip() if price else 'нет'}\n"
            f"Ссылка: https://www.avito.ru{link['href'] if link else 'нет'}"
        )

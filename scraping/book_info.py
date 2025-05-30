import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

base_url = "http://books.toscrape.com/catalogue/"

def fetchBookData(book):
    try:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text[2:]
        star = book.find('p')['class'][1]
        stock_status = book.find('p', class_='instock availability').text.strip()
        book_url = base_url + book.find('a')['href']
        genre, description = readBookInfo(book_url)

        return {
            "Titles": title,
            "Prices": price,
            "Stars": star,
            "Descriptions": description,
            "Gender": genre,
            "Stock": stock_status
        }
    except Exception as e:
        print(f'[ERROR] Failed to process book: {e}')
        return None
    
def readBookInfo(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'

        sleep(randint(1, 3)) #evita bloqueio durante as requests

        soup = BeautifulSoup(response.text, 'html.parser')
        desc_div = soup.find('div', id="product_description")
        desc = desc_div.find_next_sibling('p').text if desc_div else None

        breadcrumb = soup.find('ul', class_='breadcrumb')
        genre = breadcrumb.find_all('a')[2].text.strip() if breadcrumb and len(breadcrumb.find_all('a')) >= 3 else None
        return genre, desc
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na {url}: {e}")
        return None, None
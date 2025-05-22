import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint

#TODO: - Aplicar paralelismo para diminuir o tempo de exec. 
#TODO - Modularizar e limpar o main.py

dict_stars = {"One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
        }

base_url = "http://books.toscrape.com/catalogue/"

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


def readPage(soup):
    books = soup.find_all("article", class_="product_pod")

    titles = list()
    prices = list()
    stars = list()
    descriptions = list()
    stock = list()
    gender = list()
    

    for book in books:
        titles.append(book.find('h3').find('a')['title'])
        prices.append(book.find('p', class_='price_color').text[2:])
        stars.append(book.find('p')['class'][1])
        stock.append(book.find('p', class_='instock availability').text.strip())
        new_url = base_url + book.find('a')['href']
        gen, desc = readBookInfo(new_url)
        descriptions.append(desc)
        gender.append(gen)


    data = {"Titles": titles, "Prices": prices, "Stars": stars, "Descriptions": descriptions, "Gender": gender,"Stock": stock}

    df = pd.DataFrame(data)
    df["Stars"] = df["Stars"].map(dict_stars)
    return df

dataframes = list()
num_page = 1

for page in range(1, 51): 
    url = f'http://books.toscrape.com/catalogue/page-{num_page}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    num_page += 1
    dataframes.append(readPage(soup))

    
dataframes = pd.concat(dataframes, ignore_index=True)
    
dataframes.to_csv("books.csv", index=False)
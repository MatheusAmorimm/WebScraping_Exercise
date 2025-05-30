import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from .book_info import fetchBookData
from .utils import dict_stars

def readPage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all("article", class_="product_pod")
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetchBookData, books))

    results = [r for r in results if r is not None]
    df = pd.DataFrame(results)
    df["Stars"] = df["Stars"].map(dict_stars)
    return df
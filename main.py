import pandas as pd
from scraping.pages import readPage
from concurrent.futures import ProcessPoolExecutor


if __name__ == '__main__':
    urls = [f'http://books.toscrape.com/catalogue/page-{num_page}.html' for num_page in range(1, 51)]

    with ProcessPoolExecutor() as executor:
        result = list(executor.map(readPage, urls))

    dataframes = pd.concat(result, ignore_index=True)
    dataframes.to_csv("data/books.csv", index=False, encoding='utf-8-sig')
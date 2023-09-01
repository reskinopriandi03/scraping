from typing import Any
from os.path import join
from bs4 import BeautifulSoup

from spider.config import Config as cfg

class NikeScraperDebug(object):
    def get_from_page(self) -> list[dict[str,Any]]:
        results: list[dict[str,Any]] = []
        with open(join(cfg.TEMP_DIR, "response.html"), 'r+', encoding="UTF-8") as files:
            source: str = files.read()

            #scraping process
            soup: BeautifulSoup = BeautifulSoup(source,'html.parser')
            
            product_grid = soup.find("div", attrs={"id":"skip-to-products"})
            print(product_grid)
            products = product_grid.find_all("div", attrs={"class": "product-card__body"})
            print(products)
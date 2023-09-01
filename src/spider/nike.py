from typing import Any
from httpx import Client
from bs4 import BeautifulSoup
from loguru import logger
from typing import Optional

from spider.helper import FileHelper
from spider.config import Config as cfg


class NikeSpider(FileHelper):
    def __init__(self, search_query: str, locale: Optional[str]="id") -> None:
        self.search_query = search_query
        self.locale = locale
        self.base_url : str = f"https://www.nike.com/{locale}/w"
        self.client: Client = Client()
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}


    def get_pages(self):
        params: dict[str, Any] = {
            "q": self.search_query,
            "vst": self.search_query
        }

        headers: dict[str, Any] = self.user_agent
        #print(headers)
        
        #request ke website
        response = self.client.get("https://www.nike.com/id/w?q=jordan&vst=jordan", headers=headers)
        logger.debug(f"Request URL: {response.url} with Status: {response.status_code}")
        #pastikan si temporary ini dibuat 
        self.ensure_directory_exists(cfg.TEMP_DIR)

        #save hasil response ke html agar bisa debugging
        self.writetmpfile(file_name="response.html", data=response.text)
        #writetmpfile is not runing
        #so we make manually
        f = open("response.html", "w+", encoding="UTF-8")
        f.write(response.text)
        f.close()


        #proses parsing
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
    
        


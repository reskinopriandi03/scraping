from spider.nike import NikeSpider
from spider.debug import NikeScraperDebug

if __name__ == "__main__":
    """spider: NikeSpider = NikeSpider("air jordan")
    print(spider.get_pages())"""

    spider: NikeScraperDebug = NikeScraperDebug()
    datas = spider.get_from_page()
    print(datas)
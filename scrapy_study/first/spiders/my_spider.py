import scrapy


class MySpiderSpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["xxjd.shnu.edu.cn"]
    start_urls = ["http://xxjd.shnu.edu.cn/"]

    def parse(self, response):
        pass

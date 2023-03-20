import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["www.itcast.cn"]
    start_urls = ["http://www.itcast.cn/"]

    def parse(self, response):
        pass

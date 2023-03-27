import scrapy


class MySpiderSpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["xxjd.shnu.edu.cn"]
    start_urls = ["https://xxjd.shnu.edu.cn/27065/"]

    def parse(self, response):
        # 获取每个页面的链接
        number =3
        url_all1 = [f'http://xxjd.shnu.edu.cn/27065/list{i}.htm' for i in range(1, number+1)]    # 所有页面url


        for url in url_all1:
            yield response.follow(url, callback=self.parse_url, dont_filter=True)     # 访问各页面url

    # 下一页
    def parse_url(self, response):
        target_div = response.css('#wp_news_w6 > ul')
    
    # 获取<div>中的所有链接
        links = target_div.css('a::attr(href)').getall()
    
    # 对每个链接发送请求，并在回调函数中处理响应
        for link in links:
            yield response.follow(link, self.parse_page)
    def parse_page(self, response):
        # 获取所需信息
        

        title = response.css('#d-container > div > div > div > h1::text').get()
        author = response.css('#d-container > div > div > div > p > span.arti_publisher::text').get()
        timestamp = response.css('#d-container > div > div > div > p > span.arti_update::text').get()
        views = response.css('#d-container > div > div > div > p > span.arti_views::text').get()
        count=response.css('#d-container > div > div > div > p > span.arti_views > span::text').get()
        # 保存到CSV文件
        with open('data.csv', 'a') as f:
            f.write(f'{title},{author},{timestamp},{views+count}\n')




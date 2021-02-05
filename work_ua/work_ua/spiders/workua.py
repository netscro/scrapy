import scrapy


class WorkuaSpider(scrapy.Spider):
    name = 'workua'
    allowed_domains = ['work.ua']
    start_urls = ['http://work.ua/']

    def parse(self, response):
        pass

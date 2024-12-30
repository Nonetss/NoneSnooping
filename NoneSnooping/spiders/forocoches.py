import scrapy


class ForocochesSpider(scrapy.Spider):
    name = "forocoches"
    allowed_domains = ["forocoches.com"]
    start_urls = ["https://forocoches.com"]

    def parse(self, response):
        pass

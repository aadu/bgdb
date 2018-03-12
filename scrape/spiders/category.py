# -*- coding: utf-8 -*-
import scrapy


class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['boardgamegeek.com/browse/boardgamecategory']
    start_urls = ['http://boardgamegeek.com/browse/boardgamecategory/']

    def parse(self, response):
        pass

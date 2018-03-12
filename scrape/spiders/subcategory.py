import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
from scrapy.linkextractors import LinkExtractor
from scrape.items import SubcategoryItem


class SubcategoryLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip)


class SubcategorySpider(CrawlSpider):
    name = 'subcategory'
    allowed_domains = ['boardgamegeek.com']
    start_urls = ['http://boardgamegeek.com/browse/boardgamecategory/']

    rules = (
        Rule(LinkExtractor(allow=('boardgamecategory', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        loader = SubcategoryLoader(item=SubcategoryItem(), response=response)

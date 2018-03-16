CATEGORY = 'boardgamemechanic'

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
from scrapy.linkextractors import LinkExtractor
from scrape.items import MechanismItem


class MechanismLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip)
    description_out = Join()


class MechanismSpider(CrawlSpider):
    name = 'mechanic'
    allowed_domains = ['boardgamegeek.com']
    start_urls = [f'http://boardgamegeek.com/browse/{CATEGORY}/']

    rules = (
        Rule(LinkExtractor(allow=(CATEGORY, ), deny=('browse', )), callback='parse_item'),
    )

    def parse_item(self, response):
        loader = MechanismLoader(item=MechanismItem(), response=response)
        loader.add_value('id', response.url, re=r'(\d+)')
        loader.add_value('url', response.url)
        loader.add_css('name', '.geekitem_name::text')
        loader.add_css('description', '#editdesc > p')
        yield loader.load_item()

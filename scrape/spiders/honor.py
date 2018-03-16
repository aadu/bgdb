CATEGORY = 'boardgamehonor'

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
from scrapy.linkextractors import LinkExtractor
from scrape.items import HonorItem


class HonorLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip)
    description_out = Join()


class HonorSpider(CrawlSpider):
    name = 'honor'
    allowed_domains = ['boardgamegeek.com']
    start_urls = [f'http://boardgamegeek.com/browse/{CATEGORY}/']

    rules = (
        Rule(
            LinkExtractor(allow=(CATEGORY, ), deny=('browse', )),
            callback='parse_item'),
        Rule(LinkExtractor(allow=(f'{CATEGORY}/page/\d+', ), ), follow=True),
    )

    def parse_item(self, response):
        loader = HonorLoader(item=HonorItem(), response=response)
        loader.add_value('id', response.url, re=r'(\d+)')
        loader.add_value('url', response.url)
        loader.add_css('name', '.geekitem_name::text')
        loader.add_css('description', '#editdesc > p')
        yield loader.load_item()

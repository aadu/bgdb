CATEGORY = 'boardgame'
API_URL = 'https://www.boardgamegeek.com/xmlapi2/thing'
import json
import re
import urllib.parse as urlparse
from urllib.parse import urlparse, urlencode

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
from scrapy.linkextractors import LinkExtractor
from scrape.items import GameItem


class GameLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip)
    description_out = Join()


# def process_link(value):
#     print()
#     print(value)
#     print()
#     match = re.search(r'/boardgame/(\d+)/', response.url)
#     if match:
#         params = {'id': match.groups()[0]}
#         api_url = API_URL + ('&' if urlparse(API_URL).query else '?') + urlencode(params)
#         return api_url


class GameSpider(CrawlSpider):
    name = 'game'
    allowed_domains = ['boardgamegeek.com']
    start_urls = [f'http://boardgamegeek.com/browse/{CATEGORY}/']

    rules = (
        Rule(LinkExtractor(allow=(r'boardgame/\d+/', ), deny=('browse', )), callback='parse_id'),
        # Rule(LinkExtractor(allow=(r'boardgame/page/\d+', ),), follow=True),
    )

    def parse_id(self, response):
        match = re.search(r'/boardgame/(\d+)/', response.url)
        if match:
            params = {'id': match.groups()[0]}
            api_url = API_URL + ('&' if urlparse(API_URL).query else '?') + urlencode(params)
            yield scrapy.Request(api_url, callback=self.parse_item)

    def parse_item(self, response):
        l = GameLoader(item=GameItem(), selector=response.xpath('/items/item[1]'))
        l.add_value('pk', response.url, re=r'id=(\d+)')
        l.add_value('url', response.url)
        l.add_xpath('name', 'name[@type="primary"]/@value')
        l.add_xpath('description', 'description/text()')
        l.add_xpath('year_published', 'yearpublished/@value')
        l.add_xpath('min_players', 'minplayers/@value')
        l.add_xpath('max_players', 'maxplayers/@value')
        l.add_xpath('min_play_time', 'minplaytime/@value')
        l.add_xpath('max_play_time', 'maxplaytime/@value')
        l.add_xpath('min_age', 'minage/@value')
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        yield l.load_item()


#     categories = models.ManyToManyField('game.Category', blank=True, verbose_name=_('categories'))
#     subcategories = models.ManyToManyField('game.SubCategory', blank=True, verbose_name=_('subcategories'))
#     mechanics = models.ManyToManyField('game.Mechanic', blank=True, verbose_name=_('mechanics'))
#     tags = models.ManyToManyField('game.Tag', blank=True, verbose_name=_('tags'))
#     honors = models.ManyToManyField('game.Honor', blank=True, verbose_name=_('honors'))
#     publishers = models.ManyToManyField('game.Publisher', blank=True, verbose_name=_('publishers'))
#     artists = models.ManyToManyField('game.Artist', blank=True, verbose_name=_('artists'))
#     designers = models.ManyToManyField('game.Designer', blank=True, verbose_name=_('designers'))
#     reimplements = models.ManyToManyField(

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
    mechanics_out = Identity()
    subcategories_out = Identity()
    image_urls_out = Identity()
    images_out = Identity()


class GameSpider(CrawlSpider):
    name = 'game'
    allowed_domains = ['boardgamegeek.com']
    start_urls = [f'http://boardgamegeek.com/browse/{CATEGORY}/']
    custom_settings = {
        'IMAGES_STORE': 'media/games',
    }
    rules = (
        Rule(LinkExtractor(allow=(r'boardgame/\d+/', ), deny=('browse', )), callback='parse_item'),
        Rule(LinkExtractor(allow=(r'boardgame/page/\d+', ),), follow=True),
    )

    @staticmethod
    def escape(start, stop, data):
        regex = r'(?<={start}":")(.*)(?=","{stop}":)'.format(start=start, stop=stop)
        target = re.search(regex, data).groups()[0]
        escaped = re.sub(r'([^\\]")', r'\"', target)
        # escaped = re.sub(r'([^\\]\\n)', r'\\n', escaped)
        replacement = r'\1{escaped}\3'.format(escaped=escaped)
        return re.sub(r'(.*){regex}(.*)'.format(regex=regex), replacement, data)

    def load_data(self, data):
        data = self.escape('description', 'wiki', data)
        data = self.escape('wiki', 'website', data)
        return json.loads(data, strict=False)

    def parse_item(self, response):
        match = re.search(r'/boardgame/(\d+)/', response.url)
        if not match:
            return
        params = {'id': match.groups()[0]}
        api_url = API_URL + ('&' if urlparse(API_URL).query else '?') + urlencode(params)
        request = scrapy.Request(api_url, callback=self.parse_api)
        l = GameLoader(item=GameItem(), response=response)
        l.add_value('id', response.url, re=r'id=(\d+)')
        l.add_value('url', response.url)
        jsondata = response.css('script').re(r'(?<=geekitemPreload = ).*(?=;)')
        if jsondata:
            try:
                data = self.load_data(jsondata[0])
                l = self.parse_json_data(l, data)
            except:
                self.logger.warning("json fail")
                pass
        request.meta['item'] = l.load_item()
        yield request

    def parse_json_data(self, l, data):
        item = data['item']
        stats = item.get('stats')
        if stats:
            l.add_value('average_rating', stats.get('average'))
            l.add_value('num_votes', stats.get('usersrated'))
            l.add_value('complexity', stats.get('avgweight'))
        return l

    def parse_api(self, response):
        item = response.meta['item']
        l = GameLoader(item=item, selector=response.xpath('/items/item[1]'))
        l.add_value('api_url', response.url)
        l.add_xpath('image_urls', 'image/text()')
        l.add_xpath('name', 'name[@type="primary"]/@value')
        l.add_xpath('description', 'description/text()')
        l.add_xpath('year_published', 'yearpublished/@value')
        l.add_xpath('min_players', 'minplayers/@value')
        l.add_xpath('max_players', 'maxplayers/@value')
        l.add_xpath('min_play_time', 'minplaytime/@value')
        l.add_xpath('max_play_time', 'maxplaytime/@value')
        l.add_xpath('min_age', 'minage/@value')
        l.add_xpath('mechanics', 'link[@type="boardgamemechanic"]/@id')
        l.add_xpath('subcategories', 'link[@type="boardgamecategory"]/@id')
        # l.add_xpath('tags', 'link[@type="boardgamefamily"]/@id')

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

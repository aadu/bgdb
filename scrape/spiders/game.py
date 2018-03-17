CATEGORY = 'boardgame'
import json
import re

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


class GameSpider(CrawlSpider):
    name = 'game'
    allowed_domains = ['boardgamegeek.com']
    start_urls = [f'http://boardgamegeek.com/browse/{CATEGORY}/']

    rules = (
        Rule(LinkExtractor(allow=(r'boardgame/\d+/', ), deny=('browse', )), callback='parse_item'),
        # Rule(LinkExtractor(allow=(r'boardgame/page/\d+', ),), follow=True),
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
        l = GameLoader(item=GameItem(), response=response)
        l.add_value('pk', response.url, re=r'(\d+)')
        l.add_value('url', response.url)
        jsondata = response.css('script').re(r'(?<=geekitemPreload = ).*(?=;)')
        if not jsondata:
            return
        data = self.load_data(jsondata[0])
        item = data['item']
        l.add_value('name', item.get('name'))
        l.add_value('description', item.get('description'))
        l.add_value('year_published', item.get('yearpublished'))
        l.add_value('min_players', item.get('minplayers'))
        l.add_value('max_players', item.get('maxplayers'))
        l.add_value('min_play_time', item.get('minplaytime'))
        l.add_value('max_play_time', item.get('maxplaytime'))
        l.add_value('min_age', item.get('minage'))
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

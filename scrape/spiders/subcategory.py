import django
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
from scrapy.linkextractors import LinkExtractor
from ..items import SubcategoryItem

django.setup()


class SubcategoryLoader(ItemLoader):
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(str.strip)


class SubcategorySpider(CrawlSpider):
    name = 'subcategory'
    allowed_domains = ['boardgamegeek.com']
    start_urls = ['https://boardgamegeek.com/browse/boardgamecategory']

    rules = (
        Rule(LinkExtractor(allow=('boardgamecategory', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        loader = SubcategoryLoader(item=SubcategoryItem(), response=response)
        import pdb; pdb.set_trace()

        # l.add_value('league_name', 'NHL')
        # l.add_css('name', 'h1::text')
        # team = selector.css('h1::text').extract()[0]
        # if team.lower().title() in list([k for k, v in TEAM_ABBREVIATIONS.items()]):
        #     l.add_value('abbreviation', TEAM_ABBREVIATIONS.get(team.lower().title()))
        # data = l.nested_css('div.mb5 > div.c')
        # data.add_css('projected_cap_hit',
        #              'div.c > h5:nth-child(1) span::attr(data-num)')
        # data.add_css('projected_cap_space',
        #              'div.c > h5:nth-child(2) span::attr(data-num)')
        # data.add_css('projected_ltir_used',
        #              'div.c > div:nth-child(3) span::attr(data-num)')
        # data.add_css('current_cap_space',
        #              'div.c > div:nth-child(4) span::attr(data-num)')
        # data.add_css('deadline_cap_space',
        #              'div.c > div:nth-child(5) span::attr(data-num)')
        # data.add_css('todays_cap_hit',
        #              'div.c > div:nth-child(6) span::attr(data-num)')
        # data.add_css('roster_size',
        #              'div.c > div:nth-child(7)::text', re='(\d+)/\d+')
        # l.add_value('scraped_url', response.url)
        # l.add_css('logo_url', 'div#tmlogo > img::attr(src)')
        # l.add_css('image_urls', 'div#tmlogo > img::attr(src)')
        # l.add_value('scraped_html', response.text)
        # yield l.load_item()
        # if self.get_cap_hit == 'True':
        #     yield from self.parse_cap_hit(response)
        # yield from self.parse_team_stats(response)


        # item = scrapy.Item()
        # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        # item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        # return item
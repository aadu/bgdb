import scrapy
from scrapy_djangoitem import DjangoItem
from bgdb.game.models import Subcategory


class SubcategoryItem(DjangoItem):
    id = scrapy.Field()
    django_model = Subcategory

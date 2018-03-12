import scrapy
from scrapy_djangoitem import DjangoItem
from bgdb.game.models import Subcategory


class SubcategoryItem(DjangoItem):
    django_model = Subcategory

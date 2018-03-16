import scrapy

from bgdb.game.serializers import GameSerializer, SubcategorySerializer
from .utils import DRFItem


class SubcategoryItem(DRFItem):
    class Meta:
        serializer = SubcategorySerializer
        include = ['id']


class GameItem(DRFItem):
    class Meta:
        serializer = GameSerializer
        include = ['id']
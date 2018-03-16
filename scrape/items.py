import scrapy

from bgdb.game.serializers import (
    CategorySerializer,
    GameSerializer,
    SubcategorySerializer,
    MechanismSerializer,
    TagSerializer,
    HonorSerializer,
    PublisherSerializer,
    ArtistSerializer,
    DesignerSerializer,
)
from .utils import DRFItem


class CategoryItem(DRFItem):
    class Meta:
        serializer = CategorySerializer
        include = ['id']


class SubcategoryItem(DRFItem):
    class Meta:
        serializer = SubcategorySerializer
        include = ['id']


class MechanismItem(DRFItem):
    class Meta:
        serializer = MechanismSerializer
        include = ['id']


class GameItem(DRFItem):
    class Meta:
        serializer = GameSerializer
        include = ['id']


class TagItem(DRFItem):
    class Meta:
        serializer = TagSerializer
        include = ['id']


class HonorItem(DRFItem):
    class Meta:
        serializer = HonorSerializer
        include = ['id']


class PublisherItem(DRFItem):
    class Meta:
        serializer = PublisherSerializer
        include = ['id']


class ArtistItem(DRFItem):
    class Meta:
        serializer = ArtistSerializer
        include = ['id']


class DesignerItem(DRFItem):
    class Meta:
        serializer = DesignerSerializer
        include = ['id']

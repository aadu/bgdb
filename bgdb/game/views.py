import django_filters
from django_filters.filters import OrderingFilter
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from .models import Game, Mechanic, Subcategory
from .serializers import GameSerializer, MechanicSerializer, SubcategorySerializer
from ..filters import CustomOrderingFilter


class GameFilter(django_filters.FilterSet):

    class Meta:
        model = Game
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
            'year_published': ['lte', 'gte'],
            'complexity': ['lte', 'gte'],
            'average_rating': ['lte', 'gte'],
            'num_votes': ['lte', 'gte'],
            'min_players': ['lte', 'gte'],
            'max_players': ['lte', 'gte'],
            'min_play_time': ['lte', 'gte'],
            'max_play_time': ['lte', 'gte'],
            'min_age': ['lte', 'gte'],
        }

    order_by = CustomOrderingFilter(
        fields=(
            ('name', 'name'),
            ('modified', 'modified'),
            ('year_published', 'year_published'),
            ('complexity', 'complexity'),
            ('average_rating', 'average_rating'),
            ('num_votes', 'num_votes'),
        )
    )


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (AllowAny, )
    filter_class = GameFilter


class MechanicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    permission_classes = (AllowAny, )


class SubcategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = (AllowAny, )

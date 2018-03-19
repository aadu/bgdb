import django_filters
from django_filters.filters import OrderingFilter
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from .models import Game, Mechanic, Subcategory
from .serializers import GameSerializer, MechanicSerializer, SubcategorySerializer


class GameFilter(django_filters.FilterSet):

    class Meta:
        model = Game
        fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains'],
        }

    order_by = OrderingFilter(fields=(
        ('name', 'name'),
        ('modified', 'modified'),
    ))


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

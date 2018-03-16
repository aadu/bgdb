from rest_framework.serializers import ModelSerializer

from .models import Game, Category, Subcategory, Mechanism


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')


class MechanismSerializer(ModelSerializer):
    class Meta:
        model = Mechanism
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')

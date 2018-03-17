from rest_framework.serializers import ModelSerializer, IntegerField

from .models import Artist, Category, Designer, Game, Honor, Mechanic, Publisher, Subcategory, Tag


class GameSerializer(ModelSerializer):
    pk = IntegerField(read_only=False)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class MechanicSerializer(ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class HonorSerializer(ModelSerializer):
    class Meta:
        model = Honor
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class DesignerSerializer(ModelSerializer):
    class Meta:
        model = Designer
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')

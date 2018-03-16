from rest_framework.serializers import ModelSerializer

from .models import (
    Game,
    Category,
    Subcategory,
    Mechanism,
    Tag,
    Honor,
    Publisher,
    Designer,
    Artist,
)


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


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')


class HonorSerializer(ModelSerializer):
    class Meta:
        model = Honor
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')


class DesignerSerializer(ModelSerializer):
    class Meta:
        model = Designer
        fields = '__all__'
        read_only_fields = ('id', 'slug', 'modified', 'created')

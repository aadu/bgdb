from rest_framework.serializers import IntegerField, ModelSerializer

from .models import Artist, Category, Designer, Game, Honor, Mechanic, Publisher, Subcategory, Tag


class GameSerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class CategorySerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class SubcategorySerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Subcategory
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class MechanicSerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Mechanic
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class TagSerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class HonorSerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Honor
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class PublisherSerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Publisher
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class ArtistSerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Artist
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


class DesignerSerializer(ModelSerializer):
    id = IntegerField(read_only=False)

    class Meta:
        model = Designer
        fields = '__all__'
        read_only_fields = ('slug', 'modified', 'created')


from rest_framework import serializers

from .models import Category, Product, File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('id','title', 'file','file_type')
    def get_file_type(self, obj):
        return obj.get_file_type_display()


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    file_set = FileSerializer(many=True, read_only=True)
    #foo = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'avatar',
            'categories',

             'file_set',
            'url',
        )

    #def get_foo(self, obj):
    #    return 'Hello World!'

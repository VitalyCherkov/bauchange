from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url', 'label')
        extra_kwargs = {
            'url': {'view_name': 'category:posts-by-category', 'lookup_field': 'pk'},
        }
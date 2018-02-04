from rest_framework import serializers
from tag.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('url', 'label')

        extra_kwargs = {
            'url': {'view_name': 'tag:posts-by-tag', 'lookup_field': 'pk'}
        }
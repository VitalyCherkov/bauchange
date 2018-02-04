from rest_framework import serializers
from post.models import Post, Vote
from category.api.serializers import CategorySerializer
from tag.api.serializers import TagSerializer
from userprofile.api.serializers import UserProfileShortSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    likes = serializers.IntegerField(source='rating.get_likes', read_only=True)
    dislikes = serializers.IntegerField(source='rating.get_dislikes', read_only=True)
    result = serializers.SerializerMethodField()
    author = UserProfileShortSerializer()

    category = CategorySerializer()
    tag = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'url',
            'id',
            'title',
            'text',
            'pub_date',
            'likes',
            'dislikes',
            'result',
            'views',
            'category',
            'tag',
            'author'
        )

        extra_kwargs = {
            'url': {'view_name': 'post:api-detail', 'lookup_field': 'pk'},
        }

    def get_result(self, obj):
        try:
            return obj.voted_by_cur(self.context['request'].user)
        except KeyError:
            return None


class PostVotesSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(source='rating.get_likes', read_only=True)
    dislikes = serializers.IntegerField(source='rating.get_dislikes', read_only=True)
    result = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'likes', 'dislikes', 'result')

    def get_result(self, obj):
        try:
            return self.context['result']
        except KeyError:
            return None
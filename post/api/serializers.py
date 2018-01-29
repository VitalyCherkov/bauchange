from rest_framework import serializers
from post.models import Post


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
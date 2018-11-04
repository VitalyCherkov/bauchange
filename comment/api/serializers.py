from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    vote_url = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.__str__')
    avatar_url = serializers.ReadOnlyField(source='author.get_avatar_url')
    pub_date = serializers.DateTimeField(read_only=True)
    rating = serializers.IntegerField(source='rating.get_total', read_only=True)
    is_the_best=serializers.BooleanField(read_only=True)
    result = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'vote_url',
            'avatar_url',
            'text',
            'author',
            'post',
            'pub_date',
            'rating',
            'is_the_best',
            'result'
        )

    def create(self, validated_data):
        comment = Comment(
            text=validated_data['text'],
            author=validated_data['author'],
            post=validated_data['post']
        )
        comment.save()
        return comment

    def get_vote_url(self, obj):
        return obj.get_vote_url()

    def get_result(self, obj):
        try:
            return obj.voted_by_cur(self.context['user'])
        except KeyError:
            return None


class CommentVotesSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(source='rating.get_total', read_only=True)
    result = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'rating', 'result')

    def get_result(self, obj):
        try:
            return self.context['result']
        except KeyError:
            return None








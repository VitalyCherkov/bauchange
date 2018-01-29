from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.ReadOnlyField(source='author.__str__')
    pub_date = serializers.DateTimeField(read_only=True)
    rating = serializers.IntegerField(source='rating.get_total', read_only=True)
    is_the_best=serializers.BooleanField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'pub_date', 'rating', 'is_the_best')

    def create(self, validated_data):
        comment = Comment(
            text=validated_data['text'],
            author=validated_data['author'],
            post=validated_data['post']
        )
        comment.save()
        return comment


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








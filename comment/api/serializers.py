from rest_framework import serializers
from comment.models import Comment, Post, UserProfile, Vote


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'pub_date', 'is_the_best', 'rating', 'post', 'author')

    def is_valid(self, raise_exception=False):
        print('kek')
        return super(CommentSerializer, self).is_valid(raise_exception)


class AddCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.ReadOnlyField(source='author.__str__')
    pub_date = serializers.DateTimeField(read_only=True)
    rating = serializers.IntegerField(source='rating.count', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'pub_date', 'rating')

    def create(self, validated_data):
        comment = Comment(
            text=validated_data['text'],
            author=validated_data['author'],
            post=validated_data['post']
        )
        comment.save()
        return comment


class CommentVotesSerializer(serializers.ModelSerializer):
    rating = serializers.CharField(source='rating.get_total', read_only=True)
    result = serializers.SerializerMethodField()


    class Meta:
        model = Comment
        fields = ('rating', 'id', 'result')

    def get_result(self, obj):
        try:
            return self.context['result']
        except:
            return None








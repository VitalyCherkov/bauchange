from rest_framework import serializers
from comment.models import Comment, Post, UserProfile


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'pub_date', 'is_the_best', 'rating', 'post', 'author')

    def is_valid(self, raise_exception=False):
        print('kek')
        return super(CommentSerializer, self).is_valid(raise_exception)


class AddCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.first_name')
    pub_date = serializers.DateTimeField(read_only=True)
    rating = serializers.IntegerField(source='rating.count', read_only=True)

    class Meta:
        model = Comment
        fields = ('text', 'author', 'post', 'pub_date', 'rating')

    def create(self, validated_data):
        print('serializer/create')
        print(validated_data)
        comment = Comment(
            text=validated_data['text'],
            author=validated_data['author'],
            post=validated_data['post']
        )
        comment.save()
        return comment





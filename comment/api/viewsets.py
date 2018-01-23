from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from comment.api.serializers import CommentSerializer, AddCommentSerializer
from comment.models import Comment
from userprofile.models import UserProfile
from post.models import Post


class CommentViewSet(viewsets.ModelViewSet):
    CREATE_ACTION = 'create'
    DETAIL_ACTION = 'detail'
    serializers = {
        CREATE_ACTION: AddCommentSerializer,
        DETAIL_ACTION: CommentSerializer,
    }

    action = None
    queryset = Comment.comments.all()
    # serializer_class = AddCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        self.action = CommentViewSet.CREATE_ACTION
        return super(CommentViewSet, self).create(request, args, kwargs)

    def perform_create(self, serializer):
        user_profile = UserProfile.get_current_userprofile(self.request.user)
        serializer.save(author=user_profile)
        
    def retrieve(self, request, *args, **kwargs):
        self.action = CommentViewSet.DETAIL_ACTION
        print('kek lol retrieve')
        return super(CommentViewSet, self).retrieve(request, args, kwargs)
        





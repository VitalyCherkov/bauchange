from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from comment.api.serializers import CommentSerializer, AddCommentSerializer, CommentVotesSerializer
from comment.models import Comment
from userprofile.models import UserProfile


class CommentViewSet(viewsets.ModelViewSet):
    CREATE_ACTION = 'create'
    DETAIL_ACTION = 'detail'
    VOTE_ACTION = 'like'
    serializers = {
        CREATE_ACTION: AddCommentSerializer,
        DETAIL_ACTION: CommentSerializer,
        VOTE_ACTION: CommentVotesSerializer
    }

    action = None
    queryset = Comment.comments.all()
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
        return super(CommentViewSet, self).retrieve(request, args, kwargs)

    def vote(self, request, *args, **kwargs):
        self.action = CommentViewSet.VOTE_ACTION
        comment = self.get_object()

        comment.do_vote(
            user_profile=UserProfile.get_current_userprofile(request.user),
            action=request.data['action'])

        serializer = self.get_serializer(comment)
        return Response(serializer.data)
        





from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import CommentSerializer, CommentVotesSerializer
from comment.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    CREATE_ACTION = 'create'
    DETAIL_ACTION = 'detail'
    VOTE_ACTION = 'like'
    serializers = {
        CREATE_ACTION: CommentSerializer,
        DETAIL_ACTION: CommentSerializer,
        VOTE_ACTION: CommentVotesSerializer
    }

    action = None
    extra_context = {}
    queryset = Comment.comments.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_serializer_context(self):
        context = super(CommentViewSet, self).get_serializer_context()
        context.update(self.extra_context)
        return context

    def get_serializer_class(self):
        return self.serializers[self.action]

    def create(self, request, *args, **kwargs):
        self.action = CommentViewSet.CREATE_ACTION
        return super(CommentViewSet, self).create(request, args, kwargs)

    def perform_create(self, serializer):
        user_profile = self.request.user.user_profile
        serializer.save(author=user_profile)
        
    def retrieve(self, request, *args, **kwargs):
        self.action = CommentViewSet.DETAIL_ACTION
        return super(CommentViewSet, self).retrieve(request, args, kwargs)

    def vote(self, request, *args, **kwargs):
        self.action = CommentViewSet.VOTE_ACTION
        object = self.get_object()

        result = object.do_vote(
            user_profile=request.user.user_profile,
            action=request.data['action']
        )

        self.extra_context['result'] = result

        serializer = self.get_serializer(object)
        return Response(serializer.data)
        





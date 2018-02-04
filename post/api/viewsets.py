from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import PostVotesSerializer, PostSerializer
from post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    VOTE_ACTION = 'like'
    DETAIL_ACTION = 'detail'
    serializers = {
        VOTE_ACTION: PostVotesSerializer,
        DETAIL_ACTION: PostSerializer,
    }

    action = None
    extra_context = {}
    queryset = Post.posts.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_context(self):
        context = super(PostViewSet, self).get_serializer_context()
        context.update(self.extra_context)
        return context

    def get_serializer_class(self):
        return self.serializers[self.action]

    def retrieve(self, request, *args, **kwargs):
        self.action = PostViewSet.DETAIL_ACTION
        self.extra_context = {
            'request': request
        }
        return super(PostViewSet, self).retrieve(request, args, kwargs)

    def vote(self, request, *args, **kwargs):
        self.action = PostViewSet.VOTE_ACTION
        object = self.get_object()

        result = object.do_vote(
            user_profile=request.user.user_profile,
            action=request.data['action']
        )

        self.extra_context['result'] = result

        serializer = self.get_serializer(object)
        return Response(serializer.data)

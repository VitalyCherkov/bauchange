from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import PostVotesSerializer
from post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    VOTE_ACTION = 'like'
    serializers = {
        VOTE_ACTION: PostVotesSerializer
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

    def vote(self, request, *args, **kwargs):
        self.action = PostViewSet.VOTE_ACTION
        post = self.get_object()

        result = post.do_vote(
            user_profile=request.user.user_profile,
            action=request.data['action']
        )

        self.extra_context['result'] = result

        serializer = self.get_serializer(post)
        return result(serializer.data)

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import Post


class ListAllBlogPostApiView(APIView):
    """  View to list all blog post!"""
    authentication_classes = ('')
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """ Return a list of all posts. """

        posts = Post.objects.all()
        return Response(posts)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


from .models import Post
from .serializers import PostSerializer

class ListAllPostApiView(APIView):
    """  List all post or create a new post. """

    authentication_classes = ('')
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """ Return a list of all posts. """

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     """ Create and save a new post. """

    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()        
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
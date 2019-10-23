from .models import Post
from comments.models import Comment

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    """ A serializer for the Comment model """

    class Meta:
        model = Comment
        fields = (
            'comments',
            'status',
            'create_at',
            'updated_at'
        )
        extra_kwargs = {
            'create_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }


class PostSerializer(serializers.ModelSerializer):
    """ A serializer for the Blog model """

    comments = serializers.ReadOnlyField(source='comments.comment')

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'comments',
            'create_at',
            'updated_at'
        )
        extra_kwargs = {
            'create_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }

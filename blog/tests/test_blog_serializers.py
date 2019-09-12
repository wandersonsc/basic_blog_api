import pytest

from .. import serializers
from mixer.backend.django import mixer


def test_blog_serializer(db):
    """ 
    Test Blog Serializer
    """ 
    comment = mixer.blend('comments.Comment')

    data = {
        'title': "Django RestFramework rocks",
        'slug': "Django-RestFramework-rocks",
        'comments': comment
    }

    serializer = serializers.BlogSerializer(data=data)
    assert serializer.is_valid() == True
    assert serializer.errors == {}
    print(f"Errors: {serializer.errors}")

import pytest

from mixer.backend.django import mixer


@pytest.fixture
def post(db):
    """
    Setup function using Pytest fixture
    """

    comments = mixer.blend('comments.Comment')
    post = mixer.blend('blog.Post', comments=comments)
    return post

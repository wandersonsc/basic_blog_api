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


def test_blog_models(db, post):
    """
    Test Blog Models
    """ 

    assert post.pk == 1
    assert post.title == post.title

    print(" Post comments: ", post.comments)  # Run pytest -s
    print(" Post title: ", post.title)  # Run pytest -s
    print(" Post slug: ", post.slug)  # Run pytest -s


def test_return_post_title(db, post):
    """
    Test the method __str__
    """

    assert str(post) == post.title, (
        "Method '__str__' should be equal to field 'title'"
    )

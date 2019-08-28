import pytest
from mixer.backend.django import mixer


@pytest.fixture
def comment(db):
    """ 
    Setup function using pytest fixtures
    """
    comment = mixer.blend('comments.Comment')
    return comment


def test_comments_model(db, comment):
    """
    Test the Comment models
    """ 
    assert comment.pk == 1


def test_return_comment(db, comment):
    """
    Test the method __str__
    """
    assert str(comment) == comment.comments

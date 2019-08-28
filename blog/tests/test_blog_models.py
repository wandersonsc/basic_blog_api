from mixer.backend.django import mixer


def test_blog_models(db):
    """
    Test the Blog models
    """ 

    post = mixer.blend('blog.Post', title="Django - React & Redux")
    assert post.pk == 1
    assert post.title == "Django - React & Redux"


def test_return_post_title(db):
    """
    Test the method __str__
    """

    post = mixer.blend('blog.Post')
    assert str(post) == post.title, (
        "Method '__str__' should be equal to field 'title'"
    )

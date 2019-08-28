from mixer.backend.django import mixer


def test_blog_models(db):
    """
    Test the Blog models
    """ 

    comments = mixer.blend('comments.Comment')
    post = mixer.blend('blog.Post', comments=comments, title="Django - React & Redux")
    assert post.pk == 1
    assert post.title == "Django - React & Redux"

    print(" Post comments: ", post.comments)  # Run pytest -s


def test_return_post_title(db):
    """
    Test the method __str__
    """

    post = mixer.blend('blog.Post')
    assert str(post) == post.title, (
        "Method '__str__' should be equal to field 'title'"
    )

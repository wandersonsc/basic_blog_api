## Blog API

### Blog Api Using Best practices for Test Driven Development (TDD) & Pytest

Well, don't let that **basic** prefix throw you off, the main reason why I said basic_blog because we will not be using and JS frontend framework like React.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
[![Build Status](https://travis-ci.org/wandersonsc/basic_blog_api.svg?branch=master)](https://travis-ci.org/wandersonsc/basic_blog_api)

[![codecov](https://codecov.io/gh/wandersonsc/basic_blog_api/branch/master/graph/badge.svg)](https://codecov.io/gh/wandersonsc/basic_blog_api)

## Technology Stack

- Python
- Django RestFramework
- PostgreSQL
- Travis
- Pytest

## Get the code and start the server.

1. Get the code:

```
git clone https://github.com/wandersonsc/basic_blog_api
```

2. Run it! Assuming you have Python setup, run the following commands:

```
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver

```

2. Open tab to `http://127.0.0.1:8000/api/v1/` to see the main project

## Testing

To run the tests, check your test coverage, and generate a simplified coverage report & flake8:

`$ pytest or $ pytest & flake8`

```python
 def test_blog_models(db):
     """
     Test blog models
     """

    comments = mixer.blend('comments.Comment')
    post = mixer.blend(
        'blog.Post',
        comments=comments,
        title="Django - React & Redux"
        )
    assert post.pk == 1
    assert post.title == "Django - React & Redux"

```

To generate an HTML report:

    $ coverage html
    $ open htmlcov/index.html

To check the report in console::

    $ coverage report -m

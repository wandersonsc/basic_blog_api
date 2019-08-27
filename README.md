## Blog API

### Blog Api Using Best practices for Test Driven Development (TDD) & Pytest

Well, don't let that **basic** prefix throw you off, the main reason why I said basic_blog because we will not be using and JS frontend framework like React.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

## Technology Stack

- Python
- Django RestFramework
- PostgreSQL
- Travis
- Pytest

## Installation

1. Assuming you have Python setup, run the following commands:

   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser # Ah, create a superuser
   python3 manage.py runserver
   ```

2. Open tab to `http://127.0.0.1:8000/api/v1/users/` to see the main project

## Testing

To run the tests, check your test coverage, and generate a simplified coverage report & flake8:

    $ pytest
    $ flake8

```python
    def test_blog_models(db):
        """
        Test blog models
        """

        post = mixer.blend('blog.Post')
        assert post.pk == 1

```

To generate an HTML report:

    $ coverage html
    $ open htmlcov/index.html

To check the report in console::

    $ coverage report -m

## API Endpoints Quick Start Example:

```python
    class CreateUserView(generics.CreateAPIView):
        """ Create a new instance """

        serializer_class = UserSerializer
        permission_classes = (permissions.AllowAny,)
```

## Swagger Specification and Documentation

1. Open tab to `http://127.0.0.1:8000/docs/` to see the Swagger specification as well as the Documentation

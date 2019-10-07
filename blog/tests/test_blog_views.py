import pytest

from django.urls import reverse
from rest_framework.test import APIClient 
from rest_framework import status


@pytest.fixture
def apiClient():

    apiClient = APIClient()
    return apiClient


def test_endpoint_by_name(apiClient, db):
    """ Test blog endpoint '/blog/all' """

    url_path = reverse('blog:all')
    resp = apiClient.get(url_path)

    assert resp.status_code == status.HTTP_200_OK

from django.urls import path

from .views import (
    ListAllPostApiView,
)

app_name = 'blog'

urlpatterns = [
    path('posts/', ListAllPostApiView.as_view(), name='all'),
]

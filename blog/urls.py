from django.urls import path

from .views import (
    ListAllBlogPostApiView
)

app_name = 'blog'

urlpatterns = [
    path('posts/', ListAllBlogPostApiView.as_view(), name='all'),
]

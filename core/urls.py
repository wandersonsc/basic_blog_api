from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Test de endpoints",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@test.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # blog
    path('blog/', include('blog.urls', namespace='blog')),

    # auth
    path('auth/', include('djoser.urls')),

    # swagger
    path('swagger(?<format>\.json|\.yaml)',
         schema_view.without_ui(
             cache_timeout=0), 
         name='schema-json'
         ),
    path('swagger/', 
         schema_view.with_ui(
             'swagger', cache_timeout=0), 
         name='schema-swagger-ui'
         ),
    path('redoc/', 
         schema_view.with_ui(
             'redoc', cache_timeout=0), 
         name='schema-redoc'
         ),

]
if settings.DEBUG:
    # debug_toolbar settings
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

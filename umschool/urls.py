"""umschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from app_celery.celery import hello
from group.views import search
from umschool import settings

docs_schema_view = get_schema_view(
    openapi.Info(
        title='Projects API',
        default_version=f'v1',
    ), url='http://localhost:8000/docs/swagger', public=False, permission_classes=(IsAuthenticated, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
    path('',include('task.urls')),
    path('', include('post.urls')),
    path('', include('solution.urls')),
    path('', include('lesson.urls')),
    path('', include('course.urls')),
    path('', include('group.urls')),
    path('search/', search, name='search'),
    path('api/', include('api.urls')),
    path('cel/',hello),

] + static('/static' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    docs_urls = [
        path('swagger/', docs_schema_view.with_ui('swagger'), name='schema-swagger-ui'),

    ]
    urlpatterns += [path('docs/', include(docs_urls))]
"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
# schema_view = get_schema_view(title=API_TITLE)
swagger_schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version='v1'
    )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger/', swagger_schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]

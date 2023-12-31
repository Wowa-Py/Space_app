"""
URL configuration for space project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, create_user

from rest_framework.authtoken import views
from users.views import CustomAuthToken

router = DefaultRouter()
router.register('api/users', UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="User API",
        default_version='v1',
        description="API for managing users",
        terms_of_service="http://127.0.0.1:8000/api/swagger/",
        contact=openapi.Contact(email="contact@"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', create_user, name='create_user'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api-token-refresh/', views.obtain_auth_token),
]

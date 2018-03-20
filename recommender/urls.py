from django.contrib import admin
from django.conf.urls import url, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userinfo', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

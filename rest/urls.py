from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest.views import PostListCreateAPIView, PostDetailUpdateAPIView

router = routers.SimpleRouter()
router.register(
    '', PostListCreateAPIView, base_name="Posts")  # đăng ký API vào router
router.register('', PostDetailUpdateAPIView, base_name="Posts")

urlpatterns = []

urlpatterns += router.urls

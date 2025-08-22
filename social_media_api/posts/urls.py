from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

#["api/", "posts.urls"]
urlpatterns = [
    path('', include(router.urls)),
    path ("api/" ,"posts.urls"),
]

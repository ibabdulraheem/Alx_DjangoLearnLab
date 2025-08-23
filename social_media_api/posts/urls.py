from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

#social_media_api/urls.py doesn't contain: ["api/", "posts.urls"]
urlpatterns = [
    path('', include(router.urls)),
    path ("api/", "posts.urls"),
]

#["unfollow/<int:user_id>/", "follow/<int:user_id>"]
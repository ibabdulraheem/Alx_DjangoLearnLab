from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,FeedView
from . import views


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

#social_media_api/urls.py doesn't contain: ["api/", "posts.urls"]
urlpatterns = [
    path('', include(router.urls)),
    path ("api/", "posts.urls"),
    path("feed/",FeedView.as_view(), name="feed"),
    path("<int:post_id>/like/", views.like_post, name="like-post"),
    path("<int:post_id>/unlike/", views.unlike_post, name="unlike-post"),
]

#["unfollow/<int:user_id>/", "follow/<int:user_id>"]
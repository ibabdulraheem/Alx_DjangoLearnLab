from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FollowUserView, UnfollowUserView, ProfileView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

#social_media_api/urls.py doesn't contain: ["api/", "posts.urls"]
urlpatterns = [
    path('', include(router.urls)),
    path ("api/", "posts.urls"),
    path("follow_user/<int:user_id>/", FollowUserView.as_view(), name="follow_user"),
    path("unfollow_user/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow_user"),
    path("profile/<int:user_id>/", ProfileView.as_view(), name="user-profile"), #Optional
]

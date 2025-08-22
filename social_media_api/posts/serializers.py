from rest_framework import serializers
from .models import Post, Comment


#Comment Serializers
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # shows username
    post = serializers.PrimaryKeyRelatedField(read_only=True)  # post id only
    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]

#Post Serializers
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # shows username
    comments = CommentSerializer(many=True, read_only=True)  # nested comments
    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "created_at", "updated_at", "comments"]
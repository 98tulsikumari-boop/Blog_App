from rest_framework import serializers
from .models import BookMark
from app_api_account.serializers import RegisterSerializer
from app_api_blog.serializers import BlogSerializer  

class BookMarkSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d %B %Y, %I %M %p",
        read_only=True
    )
    blog_title = serializers.CharField(source='blog.title', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BookMark
        fields = ['id', 'user', 'user_name', 'blog', 'blog_title', 'created_at']
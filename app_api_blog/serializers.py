from rest_framework import serializers
from .models import Blog
from app_api_category.serializers import CategorySerializer
from app_api_tag.serializers import TagSerializer
from app_api_account.serializers import RegisterSerializer
from app_api_tag.models import Tag


class BlogSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d %B %Y, %I %M %p",
        read_only=True
    )
    category_name = serializers.CharField(source="category.name", read_only=True)
    author_name = serializers.CharField(source="author.username", read_only=True)
    tags_list = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "description",
            "content",
            "cover_image",
            "category_name",
            "tags_list",
            "author",
            "author_name",
            "created_at",
            "updated_at",
        ]

    def get_tags_list(self, obj):
        return list(obj.tags.values_list("name", flat=True))

class BlogListSerializer(serializers.ModelSerializer):
    """Simplified serializer for blog list (without full content)"""
    category_name = serializers.CharField(source="category.name", read_only=True)
    author_name = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Blog 
        fields =["id", "title", "description", "cover_image", "category_name", "author_name", "created_at"]



    

    
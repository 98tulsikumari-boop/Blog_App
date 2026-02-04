from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d %B %Y",
        read_only=True
    )
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
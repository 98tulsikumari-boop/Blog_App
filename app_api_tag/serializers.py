from rest_framework import serializers 
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%d %B %Y, %I %M %p",
        read_only=True
    )

    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ["id", "created_at"]

from django.shortcuts import render
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework import status
from app_api_account.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 
from .models import Tag 
from .serializers import TagSerializer

from django.db.models import Q
from django.db.models.query import QuerySet

# Create your views here.
# Create Tag
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_tag(request: Request) -> Response:
    name = request.data.get("name")
    # print("Tag Name: ", name)
    # return Response({"message": "Tag endpoint hit."}, status=200)

    if not name:
         return Response({"error": "Tag name should provided."}, status=400)

    # Uniqueness check
    if not Tag.objects.filter(name=name).exists():
        Tag.objects.create(name=name)

        return Response({"message": "Tag created successfully."}, status=201)
    else:
        return Response({"error": "Tag already exist."}, status=400)

# Display all Tags
@api_view(['GET'])
def display_all_tags(request: Request) -> Response:
    tags = Tag.objects.all()
    # print("Tags:", tags)
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data, status=200)

# Delete Tag
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_tag(request: Request, id: int) ->Response:
    try:
        tag = Tag.objects.get(id=id)
        tag.delete()
        return Response({"message": "Tag deleted successfully."}, status=200)
    except Tag.DoesNotExist:
        return Response({"error": "Tag not found."}, status=404)

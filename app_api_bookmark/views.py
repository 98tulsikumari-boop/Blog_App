from django.shortcuts import render
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework import status
from app_api_account.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 
from app_api_blog.models import Blog
from .models import BookMark
from app_api_blog.serializers import BlogSerializer, BlogListSerializer 
from .serializers import BookMarkSerializer

from django.db.models import Q
from django.db.models.query import QuerySet


# Create your views here.
# Bookmark
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_bookmark(request: Request) -> Response:
#     user_id = request.data.get("user_id")
#     blog_id = request.data.get("blog_id")

#     if not all([user_id, blog_id]):
#         return Response({"error": "User ID and Blog Id are required!"}, status=400)

#     # Validate User
#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         return Response({"error": "User not found!"}, status=404)

#     # Validate Blog
#     try:
#         blog = Blog.objects.get(id=blog_id)
#     except Blog.DoesNotExist:
#         return Response({"error": "Blog not found!"}, status=404)

#     #  Checking if already bookmarked
#     if BookMark.objects.filter(user=user, blog=blog).exists():
#         return Response({"error": "Blog already bookmarked."}, status=400)

#     # Create Bookmarked
#     bookmark = BookMark.objects.create(user=user, blog=blog)
#     serializer = BookMarkSerializer(bookmark)

#     return Response({
#         "message": "Blog Bookmarked successfully!",
#         "data": serializer.data
#     }, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_bookmark(request: Request) -> Response:
    user = request.user
    blog_id = request.data.get("blog_id")

    if not blog_id:
        return Response({"error": "Blog ID is required!"}, status=400)

    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return Response({"error": "Blog not found!"}, status=404)

    if BookMark.objects.filter(user=user, blog=blog).exists():
        return Response({"error": "Blog already bookmarked."}, status=400)

    bookmark = BookMark.objects.create(user=user, blog=blog)
    serializer = BookMarkSerializer(bookmark)

    return Response({
        "message": "Blog bookmarked successfully!",
        "data": serializer.data
    }, status=201)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_bookmark(request: Request, blog_id: int) -> Response:
    user_id = request.data.get("user_id") or (request.user.id if getattr(request.user, 'is_authenticated', False) else None)

    if not user_id:
        return Response({"error": "User ID is required"}, status=400)

    try:
        bookmark = BookMark.objects.get(user_id=user_id, blog_id=blog_id)
        bookmark.delete()
        return Response({"message": "Bookmark removed successfully."}, status=200)
    except BookMark.DoesNotExist:
        return Response({"error": "Bookmark not found"}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_bookmarks(request: Request) -> Response:
    user = request.user

    bookmarks = BookMark.objects.filter(user=user).select_related('blog')

    if not bookmarks.exists():
        return Response({"message": "No bookmarks found."}, status=200)

    blogs = [bookmark.blog for bookmark in bookmarks]
    serializer = BlogSerializer(blogs, many=True)

    return Response(serializer.data, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_bookmark(request: Request, blog_id: int) -> Response:
    """Check if blog is bookmarked (Logged-in users)"""
    is_bookmarked = BookMark.objects.filter(user=request.user, blog_id=blog_id).exists()

    return Response({
        'is_bookmarked': is_bookmarked
    }, status=200)

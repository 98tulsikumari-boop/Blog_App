from django.shortcuts import render
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework import status
from app_api_account.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 
from .models import Blog
from app_api_tag.models import Tag
from .serializers import BlogSerializer, BlogListSerializer
from app_api_tag.serializers import TagSerializer

from django.db.models import Q
from django.db.models.query import QuerySet
from app_api_category.models import Category

# Create Blog
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request: Request) -> Response:
    title = request.data.get("title")
    description = request.data.get("description", "")
    content = request.data.get("content")
    category_id = request.data.get("category")
    tag_ids = request.data.get("tags", [])
    cover_image = request.FILES.get("cover_image")

    if not all([title, content, category_id]):
        return Response(
            {"error": "title, content and category are required"},
            status=400
        )

    if Blog.objects.filter(title=title).exists():
        return Response({"error": "Title already exists"}, status=400)

    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({"error": "Invalid category"}, status=400)

    blog = Blog.objects.create(
        author=request.user,
        title=title,
        description=description,
        content=content,
        category=category,
        cover_image=cover_image
    )

    #  Set tags AFTER creation
    if tag_ids:
        valid_tags = Tag.objects.filter(id__in=tag_ids)

        if valid_tags.count() != len(tag_ids):
            return Response(
                {"error": "One or more tags are invalid"},
                status=status.HTTP_400_BAD_REQUEST
            )

    blog.tags.set(valid_tags)

    serializer = BlogSerializer(blog)
    return Response(serializer.data, status=201)

# Display All Blogs
@api_view(['GET'])
def display_all_blog(request: Request) -> Response:
    if request.method == "GET":
        blogs: QuerySet = Blog.objects.select_related('category', 'author').prefetch_related('tags')

        # Optional filters
        category = request.GET.get("category")
        tag = request.GET.get("tag")
        search = request.GET.get("search")

        if category:
            blogs = blogs.filter(category__name__iexact=category)

        if tag:
            blogs = blogs.filter(tags__name__iexact=tag).distinct()

        if search:
            blogs = blogs.filter(
                Q(title__icontains=search)  |  Q(content__icontains=search)
            )

        serializer = BlogListSerializer(blogs, many=True)
        return Response(serializer.data, status=200)  # 200  -> OK

# Display Blog With ID
@api_view(['GET'])
def display_blog(request: Request, id: int) -> Response:
    try:
        blog = Blog.objects.select_related("category", "author").prefetch_related("tags").get(id=id)
    except Blog.DoesNotExist:
        return Response({"error": "Blog not found"}, status=404)  # 404-> Not Found

    serializer = BlogSerializer(blog)
    return Response(serializer.data, status=200)

# Update Blog with ID
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def Update_put_api(request: Request, id: int) -> Response:
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response({"error": "Blog not found"}, status=404)

    if blog.author != request.user:
        return Response({"error": "Not allowed"}, status=403)

    title = request.data.get("title")
    description = request.data.get("description")
    content = request.data.get("content")
    category_id = request.data.get("category")
    tag_ids = request.data.get("tags")

    if title:
        if Blog.objects.filter(title=title).exclude(id=id).exists():
            return Response({"error": "Title already exists"}, status=400)
        blog.title = title

    if description is not None:
        blog.description = description

    if content:
        blog.content = content

    if category_id:
        try:
            blog.category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Invalid category"}, status=400)

    if isinstance(tag_ids, list):
        blog.tags.set(tag_ids)

    blog.save()
    serializer = BlogSerializer(blog)

    return Response(serializer.data, status=200)

# Delete Blog with ID
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blog(request: Request, id: int) -> Response:
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response({"error": "Blog not found"}, status=404)

    if blog.author != request.user:
        return Response({"error": "Not allowed"}, status=403)

    blog.delete()
    return Response({"message": "Blog deleted"}, status=200)


# Filter Blog by Category, Tag and Category + Tag
@api_view(['GET'])
def filter_blogs(request: Request) -> Response:
    category = request.GET.get("category")
    tag = request.GET.get("tag")
    search = request.GET.get("search")

    blogs = Blog.objects.all()

    if category:
        blogs = blogs.filter(category__name__iexact=category)

    if tag:
        blogs = blogs.filter(tags__name__iexact=tag).distinct()

    if search:
        blogs = blogs.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        )

    if not blogs.exists():
        return Response({"message": "No blogs found"}, status=404)

    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=200)


# ------------------------------------------


    







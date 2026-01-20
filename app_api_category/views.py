from django.shortcuts import render
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view   
from .models import Category
from .serializers import CategorySerializer

from django.db.models import QuerySet 

# Create your views here.

# -----------------------------------------------------
# Create Your View for Category
# Create Category
@api_view(['POST'])
def create_category(request: Request) -> Response:
    name = request.data.get("name")
    description = request.data.get("description")

    if not name:
        return Response({"error": "Category name should provided."}, status=400)

    # Uniqeness check
    if not Category.objects.filter(name=name).exists():
        Category.objects.create(name=name, description=description)

        return Response({"message": "Category created successfully!"}, status=201)
    else:
        return Response({"error": "Category already exist"}, status=400)

# Display Category
@api_view(['GET'])
def categories_list(request: Request) -> Response:
    if request.method == "GET":
        categories = Category.objects.all()
        return Response(
            [{"id": category.id, "name": category.name, "description": category.description} for category in categories]
        )
        # serializer = CategorySerializer(categories, many=True)
        # return Response(serializer.data, status=200)

# Update Category with ID
@api_view(['PUT'])
def update_category(request: Request, id: int) ->Response:
    name = request.data.get("name")
    description = request.data.get("description")

    # Uniqeness check
    if Category.objects.filter(name=name).exclude(id=id).exists():
        return Response({"error": "This ctaegory already exist."}, status=400)

    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)

    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    else:
        return Response(serializer.errors, status=400)

# Delete Category with ID
@api_view(['DELETE'])
def delete_category(request: Request, id: int) ->Response:
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return Response({"message": "Category deleted successfully"}, status=200)
    except Category.DoesNotExist:
        return Response({"error": "Category not found"}, status=404)
        
# ----------------------------------------------------------------------------------

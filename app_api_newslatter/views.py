from django.shortcuts import render
from rest_framework.request import Request 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Subscriber
from .serializers import SubscriberSerializer

# Create your views here.
@api_view(['POST'])
def subscribe_blog(request: Request) -> Response:
    email = request.data.get("email")

    if not email:
        return Response({
            "error": "Email is required"}, status=400)
        

    if Subscriber.objects.filter(email=email).exists():
        return Response({"message": "There is already one subscriber with this email."}, status=400)

    serializer = SubscriberSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response({"error": "Invalid email!"}, status=400)

@api_view(['GET'])
def subscribers_list(request: Request) -> Response:
    subscribers: QuerySet = Subscriber.objects.all()
    serializer = SubscriberSerializer(subscribers, many=True)
    return Response(serializer.data, status=200)



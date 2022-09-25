from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from base.models import User

from base.api import serializers


@api_view(['GET'])
def Routes(request):
    routes = [
        'GET /api/User',
        'All CRUD OPERATIONS',
        'UserList: view all users',
        'Userdetail: view one user with id',
        'UserCreate: Create a user',
        'UserUpdate: update a user',
        'UserDelete: Delete a User',
        
    ]
    return Response (routes)

@api_view(['GET'])
def UserList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def Userdetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many = False)

    return Response(serializer.data)

@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UserUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data = request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def UserDelete(request, pk):
    user = User.objects.get(id=pk)
    
    user.delete()

    return Response("User is deleted.")
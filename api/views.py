from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from superuser import models
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login, logout

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def loginUser(request):
    context = {}
    user = models.User.objects.get(pk=request.user.id)
    login(request, user)
    context.update({'message': "User Logged In Successfully"})
    return Response(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logoutUser(request):
    context = {}
    logout(request)
    try:
        del request.session
    except:
        pass
    try:
        storage = get_messages(request)
        for message in storage:
            message = ''
        storage.used = False
    except:
        pass
    context.update({'message': "Logged Out Successfully"})
    return Response(context)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserDetails(request):
    context = {}
    context.update({'message': "User Details Fetched Successfully", 'userDetails': {'id': request.user.id, 'email': request.user.email, 'username': request.user.username, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone': request.user.phone}})
    return Response(context)

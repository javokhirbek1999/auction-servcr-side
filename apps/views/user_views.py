from django.contrib.auth import authenticate, get_user_model
from django.http import request
from django.shortcuts import get_list_or_404, redirect
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate

from rest_framework import permissions, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.settings import api_settings

from ..serializers import user_serializer
from ..permissions import user_permissions



class UserAPIView(generics.CreateAPIView):

    """API view for User Model"""
    permission_classes = (permissions.AllowAny,)
    serializer_class = user_serializer.UserSerializer


class CreateSuperuserAPIView(generics.CreateAPIView):

    """API view for Admin Users"""
    permission_classes = (permissions.AllowAny,)
    serializer_class = user_serializer.CreateSuperuserSerializer


class UpdateDeleteUserAPIView(generics.RetrieveUpdateDestroyAPIView):

    """API view for editing and deleting users"""
    permission_classes = (user_permissions.IsOwnerOrReadOnly,)
    serializer_class = user_serializer.UserSerializer

    def get_object(self):
        return get_user_model().objects.get(user_name=self.kwargs.get('pk'))


class UpdateDeleteAdminUserAPIView(generics.RetrieveUpdateDestroyAPIView):

    """API view for editing and deleting admin users"""
    permission_classes = (user_permissions.IsAdminAndOwner,)
    serializer_class = user_serializer.CreateSuperuserSerializer

    def get_object(self):
        return get_user_model().objects.get(user_name=self.kwargs.get('pk'))


class AllUsers(generics.ListAPIView):

    """API view for retrieving details of all users (both admin and regular user details)"""
    
    permission_classes = (permissions.AllowAny,)
    serializer_class = user_serializer.UserSerializer
    queryset = get_user_model().objects.all()
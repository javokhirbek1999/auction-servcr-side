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
from ..models.user import User



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
    
    # def update(self, request, *args, **kwargs):

    #     self.user = self.get_object()   
        
    #     if self.user is None:
    #         return Response({
    #             'status': 'failed',
    #             'code': status.HTTP_404_NOT_FOUND,
    #             'message': 'User does not exist'
    #         }, status=status.HTTP_404_NOT_FOUND)

    #     user_serializer = self.get_serializer(data=request.data)

        
    #     if user_serializer.is_valid():
    #         print('IsValid')
    #         print(user_serializer.data)

    #         if not self.user.check_password(user_serializer.data.get('password')):
    #             return Response({"password": ["Wrong password"]}, status=status.HTTP_400_BAD_REQUEST)

            
    #         self.user.set_password(user_serializer.data.get('password'))
    #         self.user.save()

    #         return Response({
    #             'status': 'success',
    #             'code': status.HTTP_200_OK,
    #             'message': 'Update successful',
    #             'data': []
    #         })
        

    #     return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class AuthTokenAPIView(ObtainAuthToken):

    """API view for obtaining authentication token"""
    permission_classes = (permissions.AllowAny,)
    serializer_class = user_serializer.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


    def post(self, request, *args, **kwargs):
        
        serializer = user_serializer.AuthTokenSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.user_name,
            'email': user.email
        })
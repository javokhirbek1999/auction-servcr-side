from django.contrib.auth import get_user_model, authenticate
from django.db.models import fields
from django.utils.translation import gettext_lazy as _


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    """Serializer for User model"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'user_name', 'password', 'is_active', 'date_joined', 'date_updated')
        extra_kwargs = {
            'password': {'style': {'input_type': 'password'}, 'write_only':True, 'min_length': 5}
        }


    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        user = get_user_model().objects.get(email=validated_data['email'])

        user.set_password(validated_data['password'])
        user.save()

        validated_data['password'] = user.password

        return super().update(instance, validated_data)
    

class CreateSuperuserSerializer(serializers.ModelSerializer):

    """
    Serializer for creating Admin User
    """

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'user_name', 'password', 'date_joined', 'date_updated')
        extra_kwargs = {
            'password': {'style': {'input_type': 'password'}, 'write_only': True, 'min_length': 5}
        }


    def create(self, validated_data):
        return get_user_model().objects.create_superuser(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class AuthTokenSerializer(serializers.Serializer):
    
    """ Serializer for creating authentication token"""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )


        if not user:
            msg = _('Validation Error, invalid credentials')
            raise serializers.ValidationError(msg, code='authentication')

        
        if not user.is_active:
            msg = _('User is blocked, please contact admin')
            raise serializers.ValidationError(msg)

        attrs['user'] = user

        return attrs
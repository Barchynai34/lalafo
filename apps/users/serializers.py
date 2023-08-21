from rest_framework import serializers

from apps.users.models import User
from apps.posts.serializers import PostSerializer

from django.contrib.auth.password_validation import CommonPasswordValidator
from django.core import exceptions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'date_joined', 'profile_image')

class UserDetailSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'date_joined', 'profile_image', 'user_posts')


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=100, write_only=True
    )
    
    class Meta:
        model = User
        fields = ('username', 'profile_image', 'password', 'confirm_password')
        
    class Meta:
        model = User
        fields = ('username', 'profile_image', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})

        if attrs['password'].lower() in attrs['username'].lower():
            raise serializers.ValidationError({'password': 'Пароль слишком похож на имя пользователя'})

        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password': 'Пароль слишком короткий. Он должен содержать как минимум 8 символов.'})

        password_validator = CommonPasswordValidator()
        try:
            password_validator.validate(attrs['password'])
        except exceptions.ValidationError:
            raise serializers.ValidationError({'password': 'Пароль слишком широко распространен.'})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            profile_image=validated_data['profile_image']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
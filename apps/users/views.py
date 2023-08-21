from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.users.models import User
from apps.users.serializers import UserRegisterSerializer, UserSerialaizer, UserDetailSerializer

# Create your views here.
class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialaizer

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialaizer

class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialaizer

class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
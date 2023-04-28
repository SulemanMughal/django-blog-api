# from rest_framework import generics, permissions
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer
from rest_framework import viewsets


User = get_user_model()

class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
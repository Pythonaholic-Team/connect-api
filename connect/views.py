from django.shortcuts import render
from .models import Post
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
class PostViewsList(ListCreateAPIView):
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
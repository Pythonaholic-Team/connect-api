from django.shortcuts import render
from .models import Post, Offer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly,OfferIsOwnerOrReadOnly
from .serializers import PostSerializer, OfferSerializer


class PostViewsList(ListCreateAPIView):
    queryset = Post.objects.all().order_by("created_at")
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class OfferViewsList(ListCreateAPIView):
    queryset = Offer.objects.all().order_by("-created_at")
    serializer_class = OfferSerializer


class OfferDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (OfferIsOwnerOrReadOnly,)
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

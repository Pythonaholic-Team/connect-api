from rest_framework import serializers
from .models import Post, Offer, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ("created_at",)
        model = Offer
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ("created_at",)
        model = Comment
        fields = "__all__"

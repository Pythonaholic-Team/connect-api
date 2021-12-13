from rest_framework import serializers
from .models import Post,Offer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"



class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ('created_at',)
        model = Offer
        fields = "__all__"

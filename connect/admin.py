from django.contrib import admin
from .models import Post, Offer, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Offer)
admin.site.register(Comment)

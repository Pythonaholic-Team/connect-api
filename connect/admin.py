from django.contrib import admin
from .models import Post, Offer, Comment,Activity

# Register your models here.
admin.site.register(Post)
admin.site.register(Offer)
admin.site.register(Comment)
admin.site.register(Activity)

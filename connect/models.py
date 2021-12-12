from django.db import models
from django.utils import timezone
from accounts.models import User

class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
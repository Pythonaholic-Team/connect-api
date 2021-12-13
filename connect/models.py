from django.db import models
from django.utils import timezone
from accounts.models import User

class Post(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")


class Offer(models.Model):
    owner_id = models.ForeignKey(User , on_delete=models.CASCADE)
    to_company = models.ManyToManyField(User, related_name="companies")
    created_at = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length=255, default=True, blank=True)
    description = models.TextField()
    price = models.FloatField()
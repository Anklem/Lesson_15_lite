from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    content = models.CharField(max_length=500, default='')
    created_at = models.DateTimeField(default=timezone.now)

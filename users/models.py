from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    name = models.CharField(max_length=150, default="", blank=True, null=True)
    avatar = models.URLField(blank=True)
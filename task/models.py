from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dateCreated = models.DateTimeField('date created', auto_now_add=True)
    dateUpdated = models.DateTimeField('date updated', auto_now=True)

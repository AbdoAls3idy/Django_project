from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class boards(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description =models.CharField(max_length=200)
    def __str__(self):
        self.name
        self.description

class topic(models.Model):
    subject = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, related_name='topic', on_delete=models.CASCADE)
    board = models.ForeignKey(boards, related_name='topic', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

class posts(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(topic,related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)


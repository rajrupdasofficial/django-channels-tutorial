from tokenize import group
from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=155)
class Chat(models.Model):
    content=models.CharField(max_length=10000)
    timestamp=models.DateTimeField(auto_now=True)
    group=models.ForeignKey('Group',on_delete=models.CASCADE)



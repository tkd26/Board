from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUserModel(models.Model):
    username = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='', default='user_icon.png')

    def __str__(self):
        return self.username.username

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE, blank=True, null=True)
    images = models.ImageField(upload_to='', default='defo')
    good = models.IntegerField(null=True, blank=True, default=0)
    goodtext = models.CharField(max_length=200, null=True, blank=True, default='a ')
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=200, null=True, blank=True, default='a ')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
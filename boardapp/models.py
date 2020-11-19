from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)
    goodtext = models.CharField(max_length=200, null=True, blank=True, default='a')
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=200, null=True, blank=True, default='a')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


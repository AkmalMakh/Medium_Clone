from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, related_name='comments', on_delete=CASCADE)

    def __str__(self):
        return self.author
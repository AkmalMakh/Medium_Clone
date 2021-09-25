from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Post(models.Models):
    title = models.CharField(max_length=180)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Comment(models.Model):
    nick = models.CharField(max_length=50)
    context = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, related_name="Comments", on_delete=CASCADE)

    def __str__(self):
        return self.nick
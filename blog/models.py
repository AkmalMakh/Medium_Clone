from typing import Callable
from django.utils import timezone
from django.db import models
from django.db.models.deletion import CASCADE 
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=180)
    author = models.CharField(max_length=50)
    created_time = models.DateTimeField(default=timezone.now())
    updated_time = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments = True)

    def getAbsoluteUrl(self):
        return reverse("post:detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    #nick = models.ForeignKey('auth.User', on_delete=CASCADE)
    post = models.ForeignKey(Post, related_name="Comments", on_delete=CASCADE)
    nick = models.CharField(max_length=50)
    context = models.CharField(max_length=1000)
    commets_time = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def getAbsoluteUrl(self):
        return reverse("post:list")

    def __str__(self):
        return self.nick
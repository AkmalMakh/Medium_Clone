from datetime import time
from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.utils import timezone   

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='write something')
    author = models.ForeignKey('auth.User', on_delete=CASCADE)
    createTime = models.DateTimeField(default=timezone.now())
    publishTime = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishTime = timezone.now()
        self.save()

    def getAbsoluteUrl(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=50)
    post = models.ForeignKey(Post, related_name='comments', on_delete=CASCADE)
    content = models.TextField(default='write something')
    commentTime = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)  

    def appprove(self):
        self.approved_comments = True
        self.save()

    def getAbsoluteUrl(self):
        return reverse("post_list", kwargs={'pk':self.pk})

    def __str__(self):
        return self.author
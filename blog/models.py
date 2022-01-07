from typing import Text
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db.models.deletion import CASCADE

# Create your models here.

class Post(models.Model):
    # super user will be author
    author = models.ForeignKey('auth.User', on_delete=CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)


    def removeTextPtag(self):
        self.text = self.text.replace("<p>", "")
        self.text = self.text.replace("</p>", "")
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments = True)

    def get_absolute_url(self):
        # basically means go to url key that you have created Post
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title 

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)            


    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        # basically means go to url key that you have created Post List which home 
        return reverse("post_list", kwargs={'pk':self.pk})
    
    def __str__(self) -> str:
        return self.text

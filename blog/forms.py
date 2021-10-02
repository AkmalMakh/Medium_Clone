from django import forms
from django.db.models import fields
from django.forms import widgets
from blog.models import Comment, Post

class postForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title')

class commentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author')
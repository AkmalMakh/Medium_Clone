from django import forms
from django.db.models import fields
from django.forms import widgets
from blog.models import Comment, Post, Image

class postForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }

class commentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'content')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }

class imageForm(forms.ModelForm):

    class Meta():
        model = Image
        fields = ('title', 'image')
from django import forms
from django.db.models import fields
from django.forms import widgets
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author', 'title', 'image', 'context')

        widgets =  {
 
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
             #  we are gonna use styling libruary so that is why class name: editable medium-editor-textarea
             # we are gonna creat own class will be: textinputclass, postcontent
            'context': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):


    class Meta():

        model = Comment
        fields = ('nick', 'context')

        widgets =  {
 
            'nick': forms.TextInput(attrs={'class':'textinputclass'}),
            'context': forms.Textarea(attrs={'class':'editable medium-editor-textarea'}) 
        }

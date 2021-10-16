from django.shortcuts import render
from django.db.models import fields
from django.views.generic import(View, TemplateView, CreateView)
from . import models

# Create your views here.
class indexView(TemplateView):
    template_name = 'index.html'

class postCreateView(CreateView):
    template_name = 'postCreate.html'
    model = models.Post
    fields = ('title', 'content', 'author')
class commentCreateView(CreateView):
    template_name = 'commentCreate.html'
    model = models.Comment
    fields = ('content', 'author', 'post')
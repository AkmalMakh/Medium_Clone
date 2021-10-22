from django.shortcuts import render
from django.db.models import fields
from django.views.generic import(View, TemplateView, CreateView, DetailView)
from django.views.generic.detail import DetailView
from datetime import timezone
from . import models

# Create your views here.
class indexView(TemplateView):
    template_name = 'index.html'

# needs post list class in here as default home page

class postCreateView(CreateView):
    template_name = 'postCreate.html'
    model = models.Post
    fields = ('title', 'content', 'author')

class postDetailView(DetailView):
    context_object_name = 'post_details'
    model = models.Post
    template_name = 'templates/postDetail.html'

    def get_queryset(self):
        return models.Post.objects.filter(publishTime__lte=timezone.now().order_by('-publishTime'))

class commentCreateView(CreateView):
    template_name = 'commentCreate.html'
    model = models.Comment
    fields = ('content', 'author', 'post')
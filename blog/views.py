from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import fields
from django.views.generic import(View, TemplateView, CreateView, DetailView, ListView, DeleteView, UpdateView)
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.utils import timezone

from blog.forms import postForm
from . import models


# Create your views here.
class indexView(TemplateView):
    template_name = 'index.html'

# needs post list class in here as default home page

class postCreateView(CreateView):
    template_name = 'blog_app/postCreate.html'
    model = models.Post
    fields = ('title', 'content', 'author')
    success_url = reverse_lazy('basic_app:draftList')

class postDetailView(DetailView):
    context_object_name = 'post_details'
    model = models.Post
    template_name = 'blog_app/postDetail.html'
    
class postListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog_app/postList.html'
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(publishTime__lte=timezone.now()).order_by('-publishTime')

class postDraftListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog_app/postDraftList.html'
    model = models.Post

class postDeleteView(DeleteView):
    model = models.Post
    context_object_name = 'posts'
    template_name = 'blog_app/postDelete.html'
    success_url = reverse_lazy('basic_app:draftList')


class postUpdateView(UpdateView):
    fields = ('title', 'content')
    model = models.Post
    form_class = postForm
    success_url = reverse_lazy('basic_app:draftList')

def postUnpublish(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    post.publishTime = None
    post.save()
    return redirect('basic_app:postList')
    

def postPublish(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    post.publish()
    return redirect('basic_app:draftList')


# class commentCreateView(CreateView):
#     template_name = 'commentCreate.html'
#     model = models.Comment
#     fields = ('content', 'author', 'post')
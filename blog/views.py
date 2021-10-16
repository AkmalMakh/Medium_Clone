from django.shortcuts import render
from blog import models
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

class IndexView(TemplateView):
    template_name = "index.html"

class PostListView(ListView):
    context_object_name = "posts"
    model = models.Post
    template_name = "blog_app/post_list.html"

class PostDetailView(DetailView):
     # defining conetxt object name by default it is school_list because of we are using Listview
    context_object_name = 'post_details'
    model = models.Post
    template_name = 'blog_app/post_detail.html'

class PostCreateView(CreateView):
    fields = ('title', 'author', 'context')
    model = models.Post
    template_name = 'blog_app/update.html'

class PostUpdateView(UpdateView):
    fields = ('context')
    model = models.Post
    template_name = 'blog_app/update.html'

class CommentCreateView(CreateView):
    fields = ('post', 'nick', 'context')
    model = models.Comment
    template_name = 'blog_app/coUpdate.html'

class CommentUpdateView(CreateView):
    fields = ('context')
    model = models.Comment
    template_name = 'blog_app/coUpdate.html'


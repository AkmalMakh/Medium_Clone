from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from blog import models
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

class IndexView(TemplateView):
    template_name = "index.html"

class PostListView(ListView):
    context_object_name = "posts"
    model = models.Post
    template_name = "blog_app/post_list.html"
    
    # def get_queryset(self):
    #     return models.Post.objects.filter(published_time__lte=timezone.now()).order_by('-publisheded_time')

class PostDraftView(ListView):
    context_object_name = "posts"
    model = models.Post
    template_name = "blog_app/post_draft.html"

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
    fields = ('context',)
    model = models.Post
    template_name = 'blog_app/update.html'

def PostPublish(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.publish()
    print("???")
    return redirect("blog_app:detail", pk=pk)

def PostUnPublish(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.published_time = None
    post.save()
    print(post.published_time)
    print("Fuck")
    return redirect("blog_app:detail", pk=pk)
    
class CommentCreateView(CreateView):
    fields = ('post', 'nick', 'context')
    model = models.Comment
    template_name = 'blog_app/coUpdate.html'

class CommentUpdateView(CreateView):
    fields = ('context')
    model = models.Comment
    template_name = 'blog_app/coUpdate.html'

class PostDeleteView(DeleteView):
    model = models.Post
    template_name = 'blog_app/delete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('blog_app:list')


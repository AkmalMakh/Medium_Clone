from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from blog import models
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

from django.shortcuts import render
from .forms import PostForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = "index.html"

class PostListView(ListView):
    context_object_name = "posts"
    model = models.Post
    template_name = "blog_app/post_list.html"
    
    # def get_queryset(self):
    #     return models.Post.objects.filter(published_time__lte=timezone.now()).order_by('-publisheded_time')

class PostDraftView(LoginRequiredMixin, ListView):
    login_url ="/login/"
    context_object_name = "posts"
    model = models.Post
    template_name = "blog_app/post_draft.html"

class PostDetailView(LoginRequiredMixin, DetailView):
     # defining conetxt object name by default it is school_list because of we are using Listview
    context_object_name = 'post_details'
    model = models.Post
    template_name = 'blog_app/post_detail.html'

class PostDraftDetailView(LoginRequiredMixin, DetailView):
     # defining conetxt object name by default it is school_list because of we are using Listview
    context_object_name = 'post_details'
    model = models.Post
    
    template_name = 'blog_app/post_draft_detail.html'
    
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url ="/login/"
    fields = ('title', 'author', 'context', 'image')
    model = models.Post
    template_name = 'blog_app/update.html'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url ="/login/"
    fields = ('context',)
    model = models.Post
    template_name = 'blog_app/update.html'

def PostPublish(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.publish()
    return redirect("blog_app:detail", pk=pk)

def UnPublish(request, pk):
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

class CommentUpdateView(LoginRequiredMixin, CreateView):
    login_url ="/login/"
    fields = ('context')
    model = models.Comment
    template_name = 'blog_app/coUpdate.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url ="/login/"
    model = models.Post
    template_name = 'blog_app/delete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('blog_app:list')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'post_list.html', {'form': form, 'image': img_obj})
    else:
        form = PostForm()
    return render(request, 'post_list.html', {'form': form})


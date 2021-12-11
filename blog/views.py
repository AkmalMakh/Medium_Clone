from typing import List
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import fields
from django.views.generic import(View, TemplateView, CreateView, DetailView, ListView, DeleteView, UpdateView)
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.shortcuts import render
from .forms import imageForm

from blog.forms import postForm
from . import models


# Create your views here.
class indexView(TemplateView):
    template_name = 'index.html'

# needs post list class in here as default home page

class postCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
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

class postDraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'posts'
    template_name = 'blog_app/postDraftList.html'
    model = models.Post

class postDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = models.Post
    context_object_name = 'posts'
    template_name = 'blog_app/postDelete.html'
    success_url = reverse_lazy('basic_app:draftList')


class postUpdateView(LoginRequiredMixin, UpdateView):
    login_required = '/login/'
    model = models.Post
    form_class = postForm
    template_name = 'blog_app/postUpdate.html'
    
    def get_success_url(self):
        print(self.object.pk)   # this is getting post.pk
        return reverse('basic_app:postDetail', kwargs={'pk': self.object.pk})

class commentCreateView(CreateView):
    fields = ('author', 'content', 'post')
    model = models.Comment
    template_name = 'blog_app/commentCreate.html'
    
    def get_success_url(self):
        print(self.object.pk)   # this is getting post.pk
        return reverse('basic_app:postDetail', kwargs={'pk': self.object.post.pk})    

def imageUploadView(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'blog_app/imageUpload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = imageForm()
    return render(request, 'blog_app/imageUpload.html', {'form': form})

@login_required
def postUnpublish(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    post.publishTime = None
    post.save()
    return redirect('basic_app:postList')
    
@login_required
def postPublish(request, pk):
    post = get_object_or_404(models.Post, pk = pk)
    post.publish()
    return redirect('basic_app:draftList')


# class commentCreateView(CreateView):
#     template_name = 'commentCreate.html'
#     model = models.Comment
#     fields = ('content', 'author', 'post')
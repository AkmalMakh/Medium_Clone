from django.shortcuts import render, get_list_or_404, redirect
from django.utils import timezone
from django.views.generic import (TemplateView,DetailView,CreateView,ListView, UpdateView,DeleteView)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from blog.models import Post
from blog.forms  import PostForm, CommentForm

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

#  Posts
class PostListView(ListView):
    model = Post

    # django ORM allows to access database converting sql query 
    # https://docs.djangoproject.com/en/1.10/topics/db/queries/
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

#  Class based used of decorators to make user log in 
class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    from_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    from_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


# Comments 
@login_required
def add_comments_to_post(request, pk):
    # get single post with id
    post = get_list_or_404(Post, pk=pk)
    # check if comming request is type POST
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # checking is user form is valid before saving in db 
        if form.is_valid():
            comment = form.save(commit=False)
            # adding to specific post a comment 
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form':form})            

    
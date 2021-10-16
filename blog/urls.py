from django.urls import path
from .views import CommentCreateView, CommentUpdateView, PostCreateView, PostUpdateView, PostListView, PostDetailView
from django.conf.urls import url


app_name = 'blog_app'
urlpatterns = [
    url(r'^$', PostListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$',PostDetailView.as_view(),name='detail'),
    url(r'^create/$',PostCreateView.as_view(),name='create'),
    url(r'^coCreate/$',CommentCreateView.as_view(),name='coCreate'),
    url(r'^update(?P<pk>[-\w]+)/$',PostUpdateView.as_view(),name='update'),
   ]
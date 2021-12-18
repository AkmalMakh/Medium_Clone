from django.conf.urls import url
from django.urls import path
from blog import views
from .views import (postCreateView, postDetailView,indexView, postListView, postDraftListView, postPublish,     postDeleteView)

app_name = 'basic_app'

urlpatterns = [
    path('', postListView.as_view(), name='postList'),
    url(r'^create/$', postCreateView.as_view(), name='postCreate'),
    url(r'^(?P<pk>\d+)/$', postDetailView.as_view(), name='postDetail'),
    url(r'^post/(?P<pk>\d+)/$', views.postPublish, name='postPublish'),
    url(r'^post/(?P<pk>\d+)/delete$', postDeleteView.as_view(), name='postDelete'),
    url(r'^post/(?P<pk>\d+)/unpublish$', views.postUnpublish, name='postUnpublish'),
    url(r'^post/(?P<pk>\d+)/update/$', views.   postUpdateView.as_view(), name='postUpdate'),
    url(r'^comment/(?P<pk>\d+)/$', views.commentCreateView.as_view(), name='commentCreate'),
    path('about/', indexView.as_view(), name='about'),
    path('draft/', postDraftListView.as_view(), name='draftList'),
]
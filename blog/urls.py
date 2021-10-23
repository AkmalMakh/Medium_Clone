from django.conf.urls import url
from django.urls import path
from .views import postCreateView, indexView, postListView

app_name = 'basic_app'

urlpatterns = [
    path('', postListView.as_view(), name='postList'),
    url(r'^create/$', postCreateView.as_view(), name='postCreate'),
    path('about/', indexView.as_view(), name='about'),
]
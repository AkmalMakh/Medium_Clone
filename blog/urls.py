from django.conf.urls import url
from django.urls import path
from .views import postCreateView, commentCreateView

app_name = 'basic_app'

urlpatterns = [
    url(r'^create/$', postCreateView.as_view(), name='postCreate')
]
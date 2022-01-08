from django.urls import path
from .views import CommentCreateView, CommentUpdateView, PostCreateView, \
 PostUpdateView, PostListView, PostDetailView, PostDraftView, PostDeleteView, PostDraftDetailView
from django.conf.urls import url
from blog import views

from django.conf import settings
from django.conf.urls.static import static



app_name = 'blog_app'
urlpatterns = [
    url(r'^$', PostListView.as_view(), name="list"),
    url(r'^draft/$', PostDraftView.as_view(), name="draft"),
    url(r'^(?P<pk>\d+)/$',PostDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/draft$',PostDraftDetailView.as_view(),name='draft_detail'),
    url(r'^create/$',PostCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)$',views.PostPublish,name='postPublish'),
    url(r'^(?P<pk>\d+)/unpublish$',views.UnPublish,name='unPublish'),
    url(r'^coCreate/$',CommentCreateView.as_view(),name='coCreate'),
    url(r'^update(?P<pk>[-\w]+)/$',PostUpdateView.as_view(),name='update'),
    url(r'^delete(?P<pk>[-\w]+)/$',PostDeleteView.as_view(),name='delete'),
    path('upload/', views.image_upload_view)
   ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
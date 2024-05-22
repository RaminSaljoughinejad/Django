from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='blog-starting-page'),
    path('posts/', views.PostsView.as_view(), name='blog-post-page'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='blog-post-detail'),
    path('read-later', views.ReadLaterView.as_view(), name='read-later-url')
]
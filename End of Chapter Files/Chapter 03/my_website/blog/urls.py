from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog-starting-page'),
    path('posts/', views.posts, name='blog-post-page'),
    path('posts/<slug:slug>', views.post_detail, name='blog-post-detail')
]
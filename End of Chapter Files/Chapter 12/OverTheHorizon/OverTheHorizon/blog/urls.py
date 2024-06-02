from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='blog-root-url'),
    path('archive', views.ArchiveView.as_view(), name='blog-archive-url'),
    path('authors', views.AuthorsView.as_view(), name='blog-authors-url'),
    path('about', views.AboutView.as_view(), name='blog-about-url'),
    path('compose', views.ComposeView.as_view(), name='compose-new-post-url')
]
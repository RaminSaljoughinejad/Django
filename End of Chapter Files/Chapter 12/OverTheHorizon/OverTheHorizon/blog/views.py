from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.models import User
from .models import Post
from .forms import ComposeForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'blog/index.html'

class ArchiveView(ListView):
    template_name = 'blog/archive.html'
    model = Post
    context_object_name = 'allPosts'
    def get_queryset(self):
        return Post.objects.all().order_by('-date')

class AuthorsView(ListView):
    template_name = 'blog/authors.html'
    model = User
    context_object_name = 'authors'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class ComposeView(CreateView):
    template_name = 'blog/compose.html'
    model = Post
    form_class = ComposeForm
    success_url = reverse_lazy('blog-root-url')

    def form_valid(self, form):
        form.instance.author = self.request.user
        print("validated")
        return super().form_valid(form)
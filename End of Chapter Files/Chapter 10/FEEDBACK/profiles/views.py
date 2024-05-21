from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile


class IndexView(CreateView):
    template_name = 'profiles/index.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'

class AllProfilesView(ListView):
    template_name = 'profiles/user_profiles.html'
    model = UserProfile
    context_object_name = 'paths'


from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='profiles-root-url'),
    path('all-profiles', views.AllProfilesView.as_view(), name='all-profiles-url')
]
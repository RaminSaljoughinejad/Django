from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='vide_outlet_root'),
    path('<slug:slug>', views.movie_details, name='movie_detail_url')
]
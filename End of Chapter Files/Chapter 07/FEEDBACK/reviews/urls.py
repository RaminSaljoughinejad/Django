from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='reviews-root-url'),
    path('results', views.res, name='reviews-result-url')
]

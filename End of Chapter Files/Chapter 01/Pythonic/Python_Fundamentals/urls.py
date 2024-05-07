from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:exercise>", views.url_handler_int),
    path("<str:exercise>", views.url_handler_str, name='py_fun')
]
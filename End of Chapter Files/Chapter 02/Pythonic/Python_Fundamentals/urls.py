from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='python_fundamentals_root'),
    path("<int:exercise>", views.url_handler_int, name="py_fun_int"),
    path("<str:exercise>", views.url_handler_str, name='py_fun')
]
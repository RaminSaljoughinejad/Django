from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

_dict = {
    1:'Variables!',
    2:'If-Statements',
    3:'Loops',
    53:'This is the last notebook of this course.'
}

_redirections = {
    'intro':'1',
    'final':'53'
}


def index(request):
    response_text = "<ul>"
    for key,value in _dict.items():
        response_text+=f"<li><a href='{reverse('py_fun',args=[key])}'>Exercise {value}</a></li>"
    response_text += "</ul>"
    return HttpResponse(response_text)

# Create your views here.
def url_handler_str(request,  exercise):
    if exercise in _redirections:
        return HttpResponseRedirect(reverse('py_fun',args=[_redirections[exercise]]))
    return HttpResponse(f"The url is looking for '{exercise}' address and is a string.")


def url_handler_int(request,  exercise):
    if exercise in _dict:
        return HttpResponse(f"<h1>{_dict[exercise]}</h1>")
    else:
        return HttpResponseNotFound("<h1>This Page Does Not Exists<h1>")
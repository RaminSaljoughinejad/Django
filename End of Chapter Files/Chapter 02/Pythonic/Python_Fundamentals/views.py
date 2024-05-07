from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

_dict = {
    1:'Variables!',
    2:'If-Statements',
    3:'Loops',
    4:None,
    53:'This is the last notebook of this course.'
}

_redirections = {
    'intro':'1',
    'final':'53'
}


def index(request):
    return render(request,
                  'Python_Fundamentals/index.html',
                 {
                     "exercises": _dict
                 })

# Create your views here.
def url_handler_str(request,  exercise):
    if exercise in _redirections:
        return HttpResponseRedirect(reverse('py_fun',args=[_redirections[exercise]]))
    return HttpResponse(f"The url is looking for '{exercise}' address and is a string.")


def url_handler_int(request,  exercise):
    if exercise in _dict:
        return render(request, 'Python_Fundamentals\exercise.html', {'text':_dict[exercise], 'ex_num': exercise})
    else:
        raise Http404()
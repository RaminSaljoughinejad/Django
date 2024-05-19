from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View

class IndexView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/index.html',{
            'form':form
        })
        
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/results')
        self.get(request)


def res(request):
    return render(request, 'reviews/res.html')
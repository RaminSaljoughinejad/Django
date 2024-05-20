from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic import ListView, DetailView 
from django.views.generic.base import TemplateView 
from django.views.generic.edit import FormView
from .models import Review

class IndexView(FormView):
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "/results"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ReviewsView(ListView):
    template_name = 'reviews/all-reviews.html'
    model = Review
    context_object_name = 'reviews'

    # def get_queryset(self):
    #     base_query =  super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
        

class ThankyouView(TemplateView):
    template_name = 'reviews/res.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works" 
        return context
    
class ReviewDetailView(DetailView):
    template_name = 'reviews/review-detail.html'
    model = Review
    
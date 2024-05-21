from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic import ListView, DetailView 
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView
from .models import Review

class IndexView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "/results"

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        context["is_favorite"] = True if int(request.session.get['Favorite_review'])==loaded_review.id else False
        return context
    
    

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['Favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)
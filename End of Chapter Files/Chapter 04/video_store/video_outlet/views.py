from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.http import Http404
from django.db.models import Avg

def index(request):
    res = Movie.objects.all().order_by('title')
    count = res.count()
    avg = res.aggregate(Avg('rating'))
    return render(request, 'video_outlet/index.html',{
        'movies':res,
        'total_number_of_movies':count,
        'avg_rating':avg
    })

def movie_details(request, slug):
    res = get_object_or_404(Movie, slug=slug)
    return render(request, 'video_outlet/movie_detail.html', {
        'title':res.title,
        'rating':res.rating,
        'main_act':res.main_act,
        'is_bestselling':res.is_bestselling
    })

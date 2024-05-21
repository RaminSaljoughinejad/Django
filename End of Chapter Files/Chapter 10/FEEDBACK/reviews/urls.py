from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='reviews-root-url'),
    path('results', views.ThankyouView.as_view(), name='reviews-result-url'),
    path('reviews', views.ReviewsView.as_view(), name='all-reviews-url'),
    path('reviews/favorite', views.AddFavoriteView.as_view() ,name='favorite-review-url'),
    path('reviews/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail-url')
]

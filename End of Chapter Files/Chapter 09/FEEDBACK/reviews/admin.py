from django.contrib import admin
from .models import Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'rating')
    list_filter = ['rating']

admin.site.register(Review, ReviewAdmin)

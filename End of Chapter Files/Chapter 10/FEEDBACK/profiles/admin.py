from django.contrib import admin
from .models import UserProfile  

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')  
    search_fields = ('id', 'image')  

admin.site.register(UserProfile, UserProfileAdmin)
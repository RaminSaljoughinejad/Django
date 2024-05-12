from django.contrib import admin
from .models import Movie, Actor, Address, Language


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'postal_code', 'city']

class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address']

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('rating', 'is_bestselling')
    list_display = ['title', 'main_act']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Language, LanguageAdmin)
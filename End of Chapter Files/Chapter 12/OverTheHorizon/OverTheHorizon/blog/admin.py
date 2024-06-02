from django.contrib import admin
from .models import Post, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ['caption']

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title', 'date', 'author']
    list_filter = ('author', 'date', 'tags')

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
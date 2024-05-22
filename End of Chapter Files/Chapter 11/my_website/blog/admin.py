from django.contrib import admin
from .models import Author, Post, Tag, Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ['caption']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title', 'date', 'author']
    list_filter = ('author', 'date', 'tags')

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'post']

admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

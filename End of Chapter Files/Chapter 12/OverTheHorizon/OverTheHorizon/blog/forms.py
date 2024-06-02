from django import forms
from.models import Post


class ComposeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'excerpt', 'content', 'tags']
        labels = {
            "title":"Title",
            "excerpt":"Short overview",
            "content":"Text",
            'tags':'Tags'
        }
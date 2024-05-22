from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'All Tags'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        verbose_name_plural = 'All Authors'


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(unique=True, db_index=True)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='posts', null=True)
    excerpt = models.CharField(max_length=300)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'All Posts'

class Comment(models.Model):
    user_name = models.CharField(max_length=150)
    user_email = models.EmailField()
    text = models.TextField(max_length=500)
    post  = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name_plural = 'All Comments'
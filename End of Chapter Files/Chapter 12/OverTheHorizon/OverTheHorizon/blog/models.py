from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = 'All Tags'

class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(unique=True, db_index=True)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='images', null=True)
    excerpt = models.CharField(max_length=300)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='posts')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'All Posts'
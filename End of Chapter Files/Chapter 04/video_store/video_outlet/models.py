from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    main_act= models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("movie_detail_url", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"title:{self.title}, rating:{self.rating}, Main Actor/actress:{self.main_act}{', Best Seller' if self.is_bestselling else ''}"
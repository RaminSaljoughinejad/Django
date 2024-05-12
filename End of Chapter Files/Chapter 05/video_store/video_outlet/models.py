from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'All Languages'


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=50)

    def full_address(self):
        return f"Street: {self.street}, Postal Code: {self.postal_code}, City: {self.city}"

    def __str__(self):
        return self.full_address()
    
    class Meta:
        verbose_name_plural = 'Address Entries'


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Movie(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    main_act= models.ForeignKey(Actor, on_delete=models.CASCADE, null=True, related_name='movies')
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False, db_index=True)
    translated_to = models.ManyToManyField(Language, default=Language.objects.none)

    def get_absolute_url(self):
        return reverse("movie_detail_url", args=[self.slug])

    def __str__(self):
        return f"title:{self.title}, rating:{self.rating}, Main Actor/actress:{self.main_act}{', Best Seller' if self.is_bestselling else ''}"
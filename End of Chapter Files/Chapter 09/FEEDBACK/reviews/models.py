from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(validators=[
                                    MinValueValidator(0, message="The rating cannot be less than 0!"),
                                    MaxValueValidator(10, message="The rating cannot be More than 10!")])

    def __str__(self):
        return f'Review by {self.user_name} - Rating: {self.rating}'
    
    class Meta:
        verbose_name_plural = 'All Reviews'
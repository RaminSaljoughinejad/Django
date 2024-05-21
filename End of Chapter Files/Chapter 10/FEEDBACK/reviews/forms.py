from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ['user_name', 'review_text', 'rating']
        # exclude = ['field1', 'field2', ...]
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': "Your Rating (out of 10)"
        }
        error_messages = {
            "user_name": {
                "required":"You can Not leave this field empty!",
                "max_length": "Your name can not exceed 100 characters!"
            },
            "review_text":{
                "required":"You can NOT leave this field empty!"
            },
            "rating":{
                "required":"You can NOT leave this field empty!"
            }
        }
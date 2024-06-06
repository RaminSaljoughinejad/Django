from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django_recaptcha.fields import ReCaptchaField

class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=False)
    captcha = ReCaptchaField()

    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email', 'password1', 'password2', 'captcha', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
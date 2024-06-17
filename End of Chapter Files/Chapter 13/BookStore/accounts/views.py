from django.shortcuts import render
from django.views.generic import CreateView
from.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.conf import settings

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('custom-login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['RECAPTCHA_PUBLIC_KEY'] = settings.RECAPTCHA_PUBLIC_KEY
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        # Any additional logic can be added here
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        # Handle form errors, including reCAPTCHA errors
        return response
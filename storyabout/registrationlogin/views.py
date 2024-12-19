from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse_lazy

# Login in view
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registrationlogin/login.html'
    extra_context = {'title': 'Authorization'}
    # Dispatch method use to process requsest
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('story:stories')
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        # Add a custom error message or log
        return self.render_to_response(self.get_context_data(form=form))

# Register view
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registrationlogin/registration.html'
    extra_context = {'title': 'Registration'}
    success_url = reverse_lazy('registrationlogin:login')
    # Dispatch method use to process requsest
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('story:stories')
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        # Add a custom error message or log
        return self.render_to_response(self.get_context_data(form=form))


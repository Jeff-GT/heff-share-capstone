from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import CreateView
from .forms import SignUpForm

# Create your views here.

def LogInSuccess(request):
    return render(request, 'registration/login-success.html')

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        return reverse_lazy('login_success')
    
def logout_view(request):
    logout(request)
    return redirect('home')

class UserSignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    success_message = "Your account was created successfully. You can now log in."
    
    def form_valid(self, form):
        response = super().form_valid(form)
        return response
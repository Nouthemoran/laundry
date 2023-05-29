from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView,LogoutView

class CustomLoginView(LoginView):
	template_name = 'accounts/login.html'
	redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = 'login'
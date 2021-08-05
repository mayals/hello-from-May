from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, FormView
# from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



#------ login ---
class UserLogin(LoginView):
    template_name = 'users/login.html'
    extra_context = {
        'title': 'To DO Tasks',
        'sub_title': 'log-in',
        }



# --- logout --------#
class UserLogout(LogoutView):
    template_name = 'users/logout.html'
    



# --- register ----
class UserSignup(FormView):
    template_name = 'users/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('users:UserLogin')

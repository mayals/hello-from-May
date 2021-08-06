from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy



#------ login ---
class UserLoginView(LoginView):
    success_url = reverse_lazy('todo:tasks')
    template_name = 'users/login.html'
    extra_context = {
        'title': 'To DO Tasks',
        'sub_title': 'log-in',
        }






# --- logout --------#
class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    



# --- register ----
class UserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:UserLogin')


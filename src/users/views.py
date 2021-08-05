from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# --- register ----



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
    
    # Redirect to a success page.

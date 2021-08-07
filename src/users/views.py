from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages


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
class UserFormView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:UserLogin')
    initial = {'key': 'value'}
    

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, f'good job {user}, you are register successfuly')
            return redirect('users:UserLogin')
        
        return render(request, self.template_name, {'form': form})
        
        
       
       

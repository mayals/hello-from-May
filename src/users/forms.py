from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=30,help_text='space not allowed in username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

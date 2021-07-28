from django import forms
from .models import Task


class AddTask(forms.ModelForm):
    T_name = forms.CharField(max_length=60,label='add task')
    
    class Meta:
        model= Task
        fields = ('T_name',)


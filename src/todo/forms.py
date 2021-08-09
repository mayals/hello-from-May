from django import forms
from .models import Task
from django.core.exceptions import ValidationError

class AddTask(forms.ModelForm):
    T_name = forms.CharField(max_length=30,label='add task')
    
    class Meta:
        model= Task
        fields = ('T_name',)


    # def clean_T_name(self,request):
    #     T_name = self.request.POST['T_name']
    #     if len(T_name) > 30 : 
    #         print("ok")
    #         raise ValidationError("ops! task name is more than 30 !")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        # return T_name




class EditTask(forms.ModelForm):
    T_name = forms.CharField(max_length=30)
    
    class Meta:
        model= Task
        fields = ('T_name',)

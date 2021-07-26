from django.shortcuts import render
from django.views.generic import ListView
from .models import Task
from django.utils import timezone
# Create your views here.


class TaskListView(ListView):
   model = Task
   template_name = 'todo/index.html'
   context_object_name = 'tasks' #default is 'object_list'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['now'] = timezone.now()
       context['title'] = 'all tasks'
       return context

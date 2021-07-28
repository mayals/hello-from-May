from django.shortcuts import render
from django.views.generic import ListView
from .models import Task
from django.utils import timezone
from .forms import AddTask


# class TaskListView(ListView):
#    model = Task
#    template_name = 'todo/index.html'
#    context_object_name = 'tasks' #default is 'object_list'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['now'] = timezone.now()
#        context['title'] = 'all tasks'
#        return context


def tasks(request):
    tasks = Task.objects.filter(T_status=False)
    


    if request.method == 'POST':
        form = AddTask(request.POST) 
    else:
        form = AddTask()    
    context = {
        'tasks': tasks,
        'form' : form ,
    }
    return render(request, 'todo/index.html', context)

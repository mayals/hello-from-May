from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView
from .models import Task
from django.utils import timezone
from .forms import AddTask
from django.contrib import messages

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
    tasks = Task.objects.filter()
    if request.method == 'POST':
        form = AddTask(request.POST)
        if 'T_name' in request.POST:
            T_name = request.POST['T_name']
            if T_name:
                if form.is_valid():
                        T_name = form.cleaned_data['T_name']  
                        if T_name:
                            newtask= form.save(commit=False)
                            newtask.T_status = False
                            newtask.T_user = request.user
                            newtask= form.save()
            else:
                messages.warning(request, 'please add task.')
                return redirect('todo:tasks')
       

    else:
        form = AddTask()    
    
    
    context = {
        'tasks': tasks,
        'form' : form ,
    }
    return render(request, 'todo/index.html', context)


def change_status(request, task_id):
    tasks = Task.objects.filter()
    task = get_object_or_404(Task,id=task_id)
    if task.T_status == False:
        task.T_status = True
        task.save()
    
    elif task.T_status == True :
        task.T_status = False
        task.save()

    context ={
        'tasks': tasks,
        'task.T_status': task.T_status,
    }
    return render(request, 'todo/index.html', context)

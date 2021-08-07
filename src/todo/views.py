from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView
from .models import Task
from django.utils import timezone
from .forms import AddTask,EditTask
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# class TaskListView(ListView):
#    model = Task
#    template_name = 'todo/index.html'
#    context_object_name = 'tasks' #default is 'object_list'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['now'] = timezone.now()
#        context['title'] = 'all tasks'
#        return context




@login_required(login_url='users:UserLogin')
def tasks(request):
    tasks = Task.objects.filter(T_user=request.user)
    
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
        'tasks_done': tasks.filter(T_status=True),
        'tasks_not_done': tasks.filter(T_status=False),
        'form' : form ,
    }
    return render(request, 'todo/index.html', context)






def change_status(request, task_id):
    tasks = Task.objects.all()
    task = get_object_or_404(Task,id=task_id)
    if task.T_status == False:
        task.T_status = True
        task.save()
    
    elif task.T_status == True :
        task.T_status = False
        task.save()

    return redirect('todo:tasks')
    


def task_delete(request, task_id):
    task = get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('todo:tasks')


def tasks_not_done_delete(request):
    tasks = Task.objects.filter(T_status=False)
    tasks.delete()
    return redirect('todo:tasks')


def tasks_done_delete(request):
    tasks = Task.objects.filter(T_status=True)
    tasks.delete()
    return redirect('todo:tasks')




def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
#     editform = EditTask(instance=task)
    
#     if request.method == 'POST':
#         if 'T_name_edit' in request.POST:
#             T_name = request.POST['T_name_edit']
#             if T_name == task.T_name:
#                 editform = EditTask(instance=task, data=request.POST)
#                 if editform.is_valid():
#                     updated = editform.save(commit=False)
#                     T_name = editform.cleaned_data['T_name']
#                     updated.T_name = T_name
#                     updated.id = task_id
#                     updated.T_published = timezone.now()
#                     updated.T_user = request.user
#                     updated.save()
#     else:
#         editform = EditTask(instance=task)
    return redirect('todo:tasks',args=task_id)

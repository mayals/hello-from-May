from . import views
from django.urls import path


app_name = 'todo' 
urlpatterns =[
    # path('',views.TaskListView.as_view(),name='tasklist'),
    path('',views.tasks,name='tasks'),
    path('<int:task_id>/', views.change_status, name='change_status'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('edit/<int:task_id>/', views.task_edit, name='task_edit'),
]

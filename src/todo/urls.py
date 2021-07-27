from . import views
from django.urls import path


app_name = 'todo' 
urlpatterns =[
    # path('',views.TaskListView.as_view(),name='tasklist'),
    path('',views.tasks,name='tasks'),



]

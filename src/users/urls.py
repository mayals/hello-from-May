from django.urls import path
from . import views 


app_name = 'users'
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='UserLogin'),
    path('logout/', views.UserLogoutView.as_view(),name='UserLogout'),
    path('signup/', views.UserCreateView.as_view(), name='UserCreate'),
]

from django.urls import path
from .views import *
# signup, login, logout

urlpatterns=[
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name = 'logout')
]
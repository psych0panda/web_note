from django.urls import path
from django.contrib.auth.views import auth_login

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', auth_login, {'template_name': 'users/login.html'}, name='login'),
    path('logout', views.logout_users, name='logout'),

]

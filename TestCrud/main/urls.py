from django.urls import path
from . import views


urlpatterns = [
    path('', views.signUp, name="home"),
    path('insert', views.adduser, name='insert'),
    path('accounts', views.registered_users, name='display'),
    path('update', views.updateuser, name='update'),
]

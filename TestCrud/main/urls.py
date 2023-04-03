from django.urls import path
from . import views


urlpatterns = [
    path('', views.signUp, name="home"),
    path('insert/', views.adduser, name='insert'),
    path('accounts/', views.registered_users, name='display'),
    path('update/<int:id>/', views.updateuser, name='update'),
    path("delete/<int:id>/", views.deletedata, name="delete"),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.loginpage, name='login'),
    path('signup/', views.signuppage, name='signup'),
    path('pay/', views.paypage, name='pay'),
    path('edit/', views.editpage, name='edit'),
    path('page/', views.pagepage, name='page'),
    path('insert', views.displaydata, name='insertdata'),
]

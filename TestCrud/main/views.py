from django.shortcuts import render, redirect
from .models import User

# Create your views here.


def signUp(request):
    return render(request, 'index.html')


def adduser(request):
    if request.method == "POST":
        user = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = User(name=user, email=email, message=message)
        data.save()
        return redirect("/")

    return render(request, 'index.html')


def registered_users(request):
    data = User.objects.all()
    context = {"data": data}

    return render(request, "table.html", context)


def updateuser(request):
    return render(request, 'edit.html')

from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
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


def deletedata(request, id):
    data = User.objects.get(id=id)
    data.delete()
    

    return redirect("/accounts")


def updateuser(request, id):
    d = User.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {"d": d}

    return HttpResponse(template.render(context, request))

    
def updaterecord(request, id):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    d = User.objects.get(id=id)
    d.name = name
    d.email = email
    d.message = message
    d.save()
    return redirect("/accounts")
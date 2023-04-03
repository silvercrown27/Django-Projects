from django.shortcuts import render, redirect

from .models import User

# Create your views here.

def loginpage(request):
    return render(request, 'login.html')


def pagepage(request):
    return render(request, 'page.html')


def paypage(request):
    return render(request, 'pay.html')


def signuppage(request):
    return render(request, 'signup.html')


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        amount = request.POST.get('amount')

        query = User(name=name, email=email, age=age, contact=contact, gender=gender, amount=amount)
        query.save()

        return redirect("/")

    return render(request, 'index.html')


def displaydata(request):
    data = User.objects.all()
    context = {"data": data}

    return render(request, "index.html", context)


def deletedata(request, id):
    d = User.objects.get(id=id)
    d.delete()
    redirect("/")

    return render(request, 'index.html')


def updatedata():
    d = User.objects.get(id=id)
    redirect('update.html')


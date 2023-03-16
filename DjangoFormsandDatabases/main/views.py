from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList
from .forms import CreateNewList


# Create your views here.


def index(request):
    # ls = ToDoList.objects.get(id=id)
    return render(request, "main/list.html", {})


def home(request):
    return render(request, "main/home.html", {})


def create(request):
    form = CreateNewList()
    return render(request, "main/create.html", {"form": form})

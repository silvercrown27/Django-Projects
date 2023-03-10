from django.shortcuts import render


def homepage(requests):
    return render(requests, 'home.html')


def aboutpage(requests):
    return render(requests, 'about.html')


def services(requests):
    return render(requests, 'about.html')


def info(requests):
    return render(requests, 'about.html')


def products(requests):
    return render(requests, 'about.html')

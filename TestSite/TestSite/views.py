from django.shortcuts import render


def Home_Page(requests):
    return render(requests, 'index.html')
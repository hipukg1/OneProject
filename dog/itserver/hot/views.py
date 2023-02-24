from django.shortcuts import render


def index(request):
    return render(request, 'hot/index.html')


def about(request):
    return render(request, 'hot/about.html')
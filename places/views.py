from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def places(request):
    return render(request, 'places.html')

def add_place(request):
    return render(request, 'add_place.html')

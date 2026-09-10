from django.shortcuts import render

def home(request):
    return render(request, 'places/home.html')

def places(request):
    return render(request, 'places/places.html')

def add_place(request):
    return render(request, 'places/add_place.html')

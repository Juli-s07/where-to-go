from django.shortcuts import render
from datetime import date

def home(request):
    return render(request, 'places/home.html')

def places(request):
    return render(request, 'places/places.html')

def add_place(request):
    return render(request, 'places/add_place.html')

def place_full(request, place_id):
    place = {
        "id": place_id,
        "name": "Kyiv Coffee Place",
        "description": "A cozy place in the center of Kyiv with good coffee and a nice atmosphere.",
        "type": "Cafe",
        "location": "Kyiv, Ukraine",
        "rating": 4,
        "created_at": date(2026, 9, 11),
    }

    return render(request, "places/place_full.html", {"place": place})

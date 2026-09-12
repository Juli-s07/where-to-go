from django.shortcuts import render
from datetime import date

def home(request):
    return render(request, 'places/home.html')

def get_places(request):
    if 'places' not in request.session:
        request.session['places'] = []
    return request.session['places']

def places(request):
    places = [
        {
            "id": 1,
            "name": "Kyiv Coffee Place",
            "description": "A cozy coffee shop in the center of Kyiv with a warm atmosphere, comfortable seats, and freshly brewed coffee. It is a nice place to meet friends, read a book, or spend a quiet afternoon. The interior is simple and welcoming, and the place is especially pleasant on rainy days.",
            "type": "Cafe",
            "location": "Kyiv, Ukraine",
            "rating": 4,
            "created_at": date(2026, 9, 11),
        },
        {
            "id": 2,
            "name": "Secret Garden",
            "description": "A beautiful and peaceful hidden garden that is perfect for walking, relaxing, and taking a break from the busy city. There are lots of trees and flowers, and the quiet atmosphere makes it a great place to spend time alone or have a calm conversation with a friend. It feels like a small secret escape from the city.",
            "type": "Park",
            "location": None,
            "rating": 5,
            "created_at": date(2026, 9, 10),
        },
    ]
    return render(request, "places/places.html", {"places": places})

def add_place(request):
    return render(request, 'places/add_place.html')

def place_full(request, place_id):
    place = {
        "id": place_id,
        "name": "Kyiv Coffee Place",
        "description": "A cozy coffee shop in the center of Kyiv with a warm atmosphere, comfortable seats, and freshly brewed coffee. It is a nice place to meet friends, read a book, or spend a quiet afternoon. The interior is simple and welcoming, and the place is especially pleasant on rainy days.",
        "type": "Cafe",
        "location": "Kyiv, Ukraine",
        "rating": 4,
        "created_at": date(2026, 9, 11),
    }

    return render(request, "places/place_full.html", {"place": place})

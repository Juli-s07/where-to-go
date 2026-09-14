from django.http import Http404
from django.shortcuts import render, redirect
from datetime import date
from .default_places import DEFAULT_PLACES

def home(request):
    return render(request, 'places/home.html')

def get_user_places(request):
    return request.session.get('places', [])

def get_all_places(request):
    return DEFAULT_PLACES + get_user_places(request)

def places(request):
    places = get_all_places(request)
    return render(request, "places/places.html", {"places": places})

def add_place_to_session(request, place_data):
    user_places = get_user_places()
    place_data["id"] = f"user-{len(user_places)}"
    place_data["created_at"] = str(date.today())
    user_places.append(place_data)
    request.session['places'] = user_places

def add_place(request):
    if request.method == "POST":
        place_data = {
            "name": request.POST.get("name"),
            "description": request.POST.get("description"),
            "type": request.POST.get("type"),
            "location": request.POST.get("location"),
            "rating": int(request.POST.get("rating"))
        }
        add_place_to_session(request, place_data)
        return redirect("places:places")
    else:
        return render(request, "places/add_place.html")

def place_full(request, place_id):
    places = get_all_places(request)
    place = None
    for p in places:
        if p["id"] == place_id:
            place = p
            break
    if place is None:
        raise Http404
    return render(request, "places/place_full.html", {"place": place})

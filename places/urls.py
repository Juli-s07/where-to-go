from django.urls import path
from . import views

app_name = "places"

urlpatterns = [
    path("", views.home, name="home"),
    path("places/", views.places, name="places"),
    path("add/", views.add_place, name="add_place"),
    path("place/<int:place_id>/", views.place_full, name="place_full"),
]
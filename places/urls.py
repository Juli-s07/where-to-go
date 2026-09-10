from django.urls import path, include
from . import views

app_name = "places"

urlpatterns = [
    path("", views.home, name="home"),
    path("places/", views.places, name="places"),
    path("add/", views.add_place, name="add_place"),
]
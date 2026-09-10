from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("places/", views.places, name="places"),
    path("add/", views.add_place, name="add_place"),
]
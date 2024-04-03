from django.shortcuts import render
from . import views

urlpatters = [
    path("", views.index, name="index"),
    ]

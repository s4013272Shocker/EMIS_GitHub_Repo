from django import render,views
from . import path

urlpatterns = [
    path("", views.index, name ="index")
]

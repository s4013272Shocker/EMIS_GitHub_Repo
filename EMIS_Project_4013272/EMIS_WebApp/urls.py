from EMIS_WebApp import views
from django.urls import path

urlpatterns = [
    path("", views.index, name ="index")
]

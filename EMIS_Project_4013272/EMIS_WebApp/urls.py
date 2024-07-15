from EMIS_WebApp import views
from django.urls import path

urlpatterns = [
    path("", views.index, name ="index"),
    path ("exam", views.exam, name = "exam"),
    path ("timer", views.timer, name = "timer"),
    path ("login", views.login, name = "login"),
    path ("welcome", views.welcome, name = "welcome"),
    path("form_receipt", views.form_receipt, name = "form_receipt")
]

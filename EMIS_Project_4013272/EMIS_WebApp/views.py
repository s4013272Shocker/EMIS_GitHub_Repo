from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, "index.html")

def exam(request):
    return render (request, "exam.html")

def timer(request):
    return render (request, "timer.html")

def login(request):
    return render (request, "login.html")

def welcome(request):
    return render (request, "welcome.html")

#This verifies that the exam report has been submitted.
def form_receipt(request):
    return render (request, "form_receipt.html")
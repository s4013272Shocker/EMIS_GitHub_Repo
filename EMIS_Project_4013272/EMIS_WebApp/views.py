from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, "index.html")

def exam(request):
    return render (request, "exam.html")

def timer(request):
    return render (request, "timer.html")
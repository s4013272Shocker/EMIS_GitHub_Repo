from django.shortcuts import render
from .models import ExamReport

# Create your views here.

def index(request):
    return render (request, "index.html")

def exam(request):
    return render (request, "exam.html")

def timer(request):
    if request == "POST":
        ExamReport.moduleName = request.POST["module"]
        ExamReport.reportText = request.POST["queries"]
        ExamReport.save()
                
    return render (request, "timer.html")

def login(request):
    return render (request, "login.html")

def welcome(request):
    return render (request, "welcome.html")

#This verifies that the exam report has been submitted.
def form_receipt(request):
    return render (request, "form_receipt.html")
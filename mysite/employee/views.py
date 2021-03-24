# Create your views here.
from django.shortcuts import render,  HttpResponse
from employee . forms import StudentForm
import random


def index(request):
    student = StudentForm()
    return render(request, "index.html", {'form': student})
    return render(request, 'index.html')




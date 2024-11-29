from django.shortcuts import render
import datetime
def home(request):
    return render(request,'home.html')
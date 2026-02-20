from django.http import HttpResponse
from django.shortcuts import render

def trying(request):
    data = {
        "name": "Dhruv Vaishnav",
        "title": "Best Programmer"
    }
    return render(request,"home.html",data)

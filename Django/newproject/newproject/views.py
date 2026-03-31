from django.http import HttpResponse
from django.shortcuts import render

def fun(request):
    return render(request,"sample.html")

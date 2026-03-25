
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def fun(request):
    return HttpResponse("Dhruv is learning backend with Django")

urlpatterns = [
    path('hello/',fun),
]

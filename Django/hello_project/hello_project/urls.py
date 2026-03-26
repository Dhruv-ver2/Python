from django.contrib import admin
from django.urls import path
from .views import fun

urlpatterns = [
    path('students/',fun),

]

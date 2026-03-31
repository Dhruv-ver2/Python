#urls.py
from django.contrib import admin
from django.urls import path, include
from .views import fun

urlpatterns = [
    path('app1/', include('app1.urls')),
]

#app1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.fun, name='fun-view'),
]

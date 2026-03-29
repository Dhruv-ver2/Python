from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello_list, name="hello_list"),
]
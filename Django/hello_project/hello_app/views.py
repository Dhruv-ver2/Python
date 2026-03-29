from django.shortcuts import render
from .models import HelloItem

def hello_list(request):
    items = HelloItem.objects.all()
    return render(request, "hello_app/hello_list.html", {"items": items})
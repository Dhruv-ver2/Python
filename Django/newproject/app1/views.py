#app1/views.py
from django.shortcuts import render

def fun(request):
    return render(request, 'sample.html', {'message': 'Hello from App1!'})



from django.shortcuts import render
from django.http import HttpResponse
import datetime

def fun(request):
    # Example data to send to the template
    context = {
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
    }
    return render(request, "index.html", context)
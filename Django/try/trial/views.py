from django.http import HttpResponse
from django.shortcuts import render
import datetime

def trial(request):
    context = {
        "user_name": "Master Dhruv",
        "current_time": datetime.datetime.now(),
        "topics": ["Urls", "Views", "Templates","Dynamic Data"]
    }
    return render(request, 'index.html', context)

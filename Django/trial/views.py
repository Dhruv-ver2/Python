from django.http import HttpResponse

def fun(request):
    return HttpResponse("The code is working")
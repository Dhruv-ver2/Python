from django.http import HttpResponse

def fun(request):
    return HttpResponse("New Project has been created")

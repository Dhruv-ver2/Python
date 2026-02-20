from django.shortcuts import render
from .models import Student

def student_list(request):
    students=Student.objects.all()
    print(students)

    return render(request,"students.html",{"students.html":students})
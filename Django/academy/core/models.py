from django.db import models

class Course(models.Model):
    title=models.CharField(max_length=100)
    duration=models.IntegerField()

    def __str__(self):
        return f"Title: {self.title}\tDuration: {self.duration}"
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nCourse: {self.course}"

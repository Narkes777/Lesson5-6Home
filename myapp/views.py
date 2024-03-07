from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Student

# Create your views here.

def get_students(request):
    students = Student.objects.all()
    data = [{'name': student.name, 'age': student.age} for student in students]
    return JsonResponse(data, safe=False)



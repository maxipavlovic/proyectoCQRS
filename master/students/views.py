from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json
from .logic import logic_students as sl
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def students_view(request):
    if request.method == 'GET':
        id=request.GET.get('id',None)
        if id:
            student_dto = sl.get_student(id)
            student = serializers.serialize('json', [student_dto])
            return HttpResponse(student, 'application/json')
        else:
            students_dto = sl.get_students()
            students = serializers.serialize('json', students_dto)
            return HttpResponse(students, 'application/json')
    if request.method == 'POST':
        print(request.body)
        student_dto = sl.create_student(json.loads(request.body))
        student = serializers.serialize('json' , [student_dto,])
        return HttpResponse(student, 'application/json')
    if request.method == 'PUT' or request.method == 'PATCH':
        id=request.GET.get('id',None)
        if id:
            student_dto = sl.update_student(id, json.loads(request.body))
            student = serializers.serialize('json', [student_dto,])
            return HttpResponse(student, 'application/json')
    if request.method == 'DELETE':
        id=request.GET.get('id',None)
        if id:
            student_dto = sl.delete_student(id)
            student = serializers.serialize('json', [student_dto,])
            return HttpResponse(student, 'application/json')
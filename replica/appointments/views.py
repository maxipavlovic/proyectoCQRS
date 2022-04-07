from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json
from .logic import logic_appointments as al
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def appointments_view(request):
    if request.method == 'GET':
        id=request.GET.get('id',None)
        if id:
            appointment_dto = al.get_appointment(id)
            appointment = serializers.serialize('json', [appointment_dto])
            return HttpResponse(appointment, 'application/json')
        else:
            students_dto = al.get_appointments()
            appointments = serializers.serialize('json', students_dto)
            return HttpResponse(appointments, 'application/json')
    if request.method == 'POST':
        print(request.body)
        appointment_dto = al.create_appointment(json.loads(request.body))
        appointment = serializers.serialize('json' , [appointment_dto,])
        return HttpResponse(appointment, 'application/json')
    if request.method == 'DELETE':
        id=request.GET.get('id',None)
        if id:
            appointment_dto = al.delete_appointment(id)
            appointment = serializers.serialize('json', [appointment_dto,])
            return HttpResponse(appointment, 'application/json')
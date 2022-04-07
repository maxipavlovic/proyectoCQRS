from ..models import Appointment
from students.logic import logic_students as sl

def get_appointments():
    appointments = Appointment.objects.all()
    return appointments

def get_appointment(m_pk):
    appointment = Appointment.objects.get(pk=m_pk)
    return appointment


def create_appointment(var):
    estudiante = sl.get_student(var['estudiante'])
    appointment = Appointment(estudiante=estudiante, fechaCita=var["fechaCita"])
    appointment.save()
    return appointment

def delete_appointment(m_pk):
    appointment = get_appointment(m_pk)
    appointment.delete()
    return appointment
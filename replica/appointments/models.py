from django.db import models
from students.models import Student
from dj_cqrs.mixins import ReplicaMixin

class Appointment(ReplicaMixin, models.Model):
    
    CQRS_ID = 'appointment'

    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        print(mapped_data)

    estudiante = models.ForeignKey(Student, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaCita = models.DateTimeField()

    def __str__(self):
        return '%s %s' % (self.fechaCreacion, self.fechaCita)
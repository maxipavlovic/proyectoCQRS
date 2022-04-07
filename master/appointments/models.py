from django.db import models
from students.models import Student
from dj_cqrs.mixins import MasterMixin

class Appointment(MasterMixin, models.Model):
    CQRS_ID = 'appointment'

    estudiante = models.ForeignKey(Student, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaCita = models.DateTimeField()

    def __str__(self):
        return '%s %s' % (self.fechaCreacion, self.fechaCita)
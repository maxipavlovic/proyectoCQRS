from django.db import models
from dj_cqrs.mixins import MasterMixin

class Student(MasterMixin, models.Model):
    CQRS_ID = 'student'
    CQRS_PRODUCE = True
    identificacion = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    universidad = models.CharField(max_length=50)
    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.identificacion)
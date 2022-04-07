from ..models import Student

def get_students():
    students = Student.objects.all()
    return students

def get_student(m_pk):
    student = Student.objects.get(pk=m_pk)
    return student

def update_student(m_pk, new_var):
    student = get_student(m_pk)
    student.identificacion = new_var['identificacion']
    student.nombre = new_var['nombre']
    student.correo = new_var['correo']
    student.telefono = new_var['telefono']
    student.direccion = new_var['direccion']
    student.universidad = new_var['universidad']
    student.save()
    return student

def create_student(var):
    student = Student(identificacion=var["identificacion"],nombre=var["nombre"],correo=var["correo"],telefono=var["telefono"],direccion=var["direccion"],coruniversidadreo=var["universidad"])
    student.save()
    return student

def delete_student(m_pk):
    student = get_student(m_pk)
    student.delete()
    return student
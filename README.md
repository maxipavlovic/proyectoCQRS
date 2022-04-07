# Proyecto CQRS Arquisoft

Este proyecto muestra la implementación de una arquitectura CQRS. En este caso se busca correr todo en una misma máquina, no obstante replicar esto en varias maquinas es equivalente a separar las aplicaciones en cada una.

Los siguientes pasos deben hacerse para correrse el proyecto:
1. Crear las bases de datos en postgres para la aplicación master y replica. Con esta información se deben cambiar los archivos settings.py para agregar el nombre de la base de datos y las credenciales de postgres.
2. Correr el proyecto master con python manage.py runserver.
3. Ejecutar el escuchador del proyecto replica con python manage.py cqrs_consume -w 2. Para verificar la actualización se puede correr este proyecto también.
4. Cada vez que haya algún cambio en el proyecto master (encargado de cambios en la base de datos) se actualizara la base de datos de la replica.

## Problemas Actuales
Debido a un problema con los ids que maneja esta implementación de CQRS no se ha podido realizar la actualización inmediata. El proyecto que fue usado como base es el siguiente: https://github.com/cloudblue/django-cqrs
El problema ya fue notificado al creador de este proyecto y se espera solucionar proximamente. Resaltar que si se establece correctamente la comunicación a través de Rabbitmq entonces es un problema de la libreria.

### Soluciones parciales
Actualmente se puede manejar la actualización manualmente generando unos archivos en el master y cargandolos en el replica. Esto se debe hacer con los siguientes comandos: 


Master: python manage.py cqrs_bulk_dump --cqrs-id=student -> student.dump


Replica: python manage.py cqrs_bulk_load -i=student.dump


Esta solución es temporal y se espera poder arreglar el problema principal. No obstante, también se podría realizar una solución que permita la actualización automatica a partir de la generación de estos archivos pero no se va a intentar implementar de esta manera.

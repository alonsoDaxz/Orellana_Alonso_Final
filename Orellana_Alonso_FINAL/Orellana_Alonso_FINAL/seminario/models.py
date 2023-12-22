from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.estado}'
























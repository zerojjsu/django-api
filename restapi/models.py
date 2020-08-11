from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Homework(models.Model):
    tarea = models.CharField('Titulo de tarea', max_length=90)
    descripcion = models.TextField('Descripción', max_length=500, blank=True, default="")
    asignatura = models.CharField('Asignatura', max_length=60)
    fecha_entrega = models.DateField('Fecha de Entrega')
    nivel = models.PositiveIntegerField('Nivel de Complejidad (1 = Muy fácil ~ 5 = Muy difícil)', default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    material = models.FileField('Material de apoyo', upload_to='material/', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.tarea
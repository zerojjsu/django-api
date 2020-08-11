from rest_framework import serializers

from .models import Homework

class HomeworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'tarea', 'descripcion', 'asignatura', 'fecha_entrega', 'nivel', 'material')
        
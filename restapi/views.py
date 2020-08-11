from django.shortcuts import render

from rest_framework import viewsets
from .serializers import HomeworkSerializer
from .models import Homework


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all().order_by('tarea')
    serializer_class = HomeworkSerializer
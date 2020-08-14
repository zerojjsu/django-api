from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tareas', views.HomeworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('panel-demo', views.index, name='index'),
    path('agregarTarea', views.agregarTarea, name='agregarTarea')
]
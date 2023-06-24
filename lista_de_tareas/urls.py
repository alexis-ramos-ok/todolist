from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_de_tareas, name='lista_de_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('editar/<int:id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:id>/<str:origen>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('completar_tarea/<int:id>/', views.completar_tarea, name='completar_tarea'),
    path('completadas/', views.lista_de_tareas_completadas, name='lista_de_tareas_completadas'),
    path('volver_pendiente/<int:id>/', views.volver_tarea_pendiente, name='volver_tarea_pendiente'),
    path('about/', views.about, name='about'),
]

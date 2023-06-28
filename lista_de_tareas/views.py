from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.utils.safestring import mark_safe

def lista_de_tareas(request, dia=None):
    if dia:
        # Filtra las tareas por el día seleccionado
        tareas = Tarea.objects.filter(dia=dia, completada=False)
    else:
        # Muestra todas las tareas no completadas
        tareas = Tarea.objects.filter(completada=False)
    
    dia_seleccionado = next((k for k, v in dias.items() if v == dia), None)
 
    tareas_json = mark_safe(serialize('json', Tarea.objects.filter(completada=False)))
  

    response = render(request, 'lista_de_tareas.html', {'tareas': tareas, 'dia': dia, 'dia_seleccionado': dia_seleccionado, 'tareas_json': tareas_json})
    
    return response



def crear_tarea(request, dia):
    tareas = Tarea.objects.filter(dia=dia, completada=False)
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.dia = dia
            tarea.save()
            return redirect('lista_de_tareas', dia=dia)
        else:
            print('El formulario no es válido:', form.errors)
    else:
        form = TareaForm()
    tareas_json = mark_safe(serialize('json', Tarea.objects.filter(completada=False)))
    return render(request, 'crear_tarea.html', {'form': form, 'dia': dia, 'tareas_json': tareas_json})


def editar_tarea(request, id, dia):
    tarea = get_object_or_404(Tarea, id=id)
    tareas = Tarea.objects.filter(dia=dia, completada=False)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_de_tareas', dia=tarea.dia)  # Modificación aquí
    else:
        form = TareaForm(instance=tarea)
        tareas_json = mark_safe(serialize('json', Tarea.objects.filter(completada=False)))
        return render(request, 'editar_tarea.html', {'form': form, 'dia': dia, 'tareas_json': tareas_json})



def eliminar_tarea(request, id, origen, dia=None):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    if origen == 'lista_de_tareas':
        return redirect('lista_de_tareas', dia=dia)
    else:
        return redirect('lista_de_tareas_completadas', dia=dia)



@csrf_exempt
def completar_tarea(request, id):
    if request.method == 'POST':
        tarea = get_object_or_404(Tarea, id=id)
        tarea.completada = True
        tarea.save()
    return HttpResponse('')

def lista_de_tareas_completadas(request, dia):
    if dia:
        # Filtra las tareas completadas por el día seleccionado
        tareas = Tarea.objects.filter(dia=dia, completada=True)
    else:
        # Muestra todas las tareas completadas
        tareas = Tarea.objects.filter(completada=True)
    tareas_json = mark_safe(serialize('json', Tarea.objects.filter(completada=False)))
    return render(request, 'lista_de_tareas_completadas.html', {'tareas': tareas, 'dia': dia, 'tareas_json': tareas_json})


def volver_tarea_pendiente(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.completada = False
    tarea.save()
    return redirect('lista_de_tareas_completadas', dia=tarea.dia)


def about(request):
    return render(request, 'about.html')

dias = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}

def dias_de_la_semana(request):
    tareas = Tarea.objects.all()
    tareas_json = mark_safe(serialize('json', Tarea.objects.filter(completada=False)))
    return render(request, 'dias_de_la_semana.html', {'dias': dias, 'tareas_json': tareas_json})
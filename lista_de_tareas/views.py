from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.views.decorators.csrf import csrf_exempt

def lista_de_tareas(request):
    tareas = Tarea.objects.filter(completada=False)
    return render(request, 'lista_de_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_de_tareas')
        else:
            print('El formulario no es válido:', form.errors)
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})


def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_de_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'editar_tarea.html', {'form': form})

def eliminar_tarea(request, id, origen):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    if origen == 'lista_de_tareas':
        return redirect('lista_de_tareas')
    else:
        return redirect('lista_de_tareas_completadas')


@csrf_exempt
def completar_tarea(request, id):
    if request.method == 'POST':
        tarea = get_object_or_404(Tarea, id=id)
        tarea.completada = True
        tarea.save()
    return HttpResponse('')

def lista_de_tareas_completadas(request):
    tareas = Tarea.objects.filter(completada=True)
    return render(request, 'lista_de_tareas_completadas.html', {'tareas': tareas})

def volver_tarea_pendiente(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.completada = False
    tarea.save()
    return redirect('lista_de_tareas_completadas')

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "inicio.html")

def recetas(request):
    lista = Receta.objects.all()
    return render(request, "recetas.html", {"recetas": lista})

def nutricion(request):
    lista = Nutricion.objects.all()
    return render(request, "nutricion.html", {"nutricion": lista})

def deportes(request):
    lista = Deportes.objects.all()
    return render(request, "deportes.html", {"deportes": lista})

def agregar_receta(request):
    
    if request.method == 'POST':
        mi_formulario = Agregar_Recetas(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            Receta.objects.create(
                titulo = data['titulo'],
                sabor = data['sabor'],
                ingredientes = data['ingredientes'],
                tiempo_coccion = data['tiempo_coccion'],
                instrucciones = data['instrucciones']
            )
        return render(request, "inicio.html")
    else:
        mi_formulario = Agregar_Recetas()
        return render(request, "agregar_receta.html", {"mi_formulario": mi_formulario})
    
def agregar_nutricion(request):
    if request.method == 'POST':
        mi_formulario = Agregar_Nutricion(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            nutri = Nutricion(nombre=data['nombre'], apellido=data['apellido'], matricula=data['matricula'], especialidad=data['especialidad'])
            nutri.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Agregar_Nutricion()
        return render(request, "agregar_nutricion.html", {"mi_formulario": mi_formulario})
    
def agregar_deportes(request):
    if request.method == 'POST':
        mi_formulario = Agregar_Deportes(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            depor = Deportes(deporte=data['deporte'], pais=data['pais'], deportista=data['deportista'], atendido_por=data['atendido_por'])
            depor.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Agregar_Nutricion()
        return render(request, "agregar_nutricion.html", {"mi_formulario": mi_formulario})

def busqueda_matricula(request):
    return render(request, "busqueda_matricula.html")

# def buscar(request):
#     if request.GET["matricula"]:
#         matricula = request.GET["matricula"]
#         contexto = Nutricion.objects.filter(matricula__icontains=matricula)
#         return render(request, "resultados_busqueda.html", {"matricula": contexto})
#     else:
#         return HttpResponse("No existe información")    


def buscar(request):
    if request.method == "POST":
       busca_matricula = BuscarMatriculaForm(request.POST)
       if busca_matricula.is_valid():
            info = busca_matricula.cleaned_data
            matricula = Nutricion.objects.filter(matricula=info["matricula"])
            return render(request, "resultados_busqueda.html", {"matricula":matricula})
    else:
        busca_matricula = BuscarMatriculaForm
        return render(request, "busqueda_matricula.html", {"miFormulario":busca_matricula})
from django import forms

class Agregar_Recetas(forms.Form):
    titulo = forms.CharField(max_length=200)
    sabor = forms.CharField(max_length=200)
    ingredientes = forms.CharField(max_length=200)
    tiempo_coccion = forms.CharField(max_length=200)
    instrucciones = forms.CharField(max_length=200)

class Agregar_Nutricion(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    matricula = forms.CharField(max_length=20)
    especialidad = forms.CharField()

class Agregar_Deportes(forms.Form):
    deporte = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=50)
    deportista = forms.CharField(max_length=100)
    atendido_por = forms.CharField(max_length=100)


class BuscarMatriculaForm(forms.Form):
    matricula = forms.CharField(max_length=20)

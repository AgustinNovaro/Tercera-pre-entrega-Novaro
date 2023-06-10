# Tercera-pre-entrega-Novaro
Tercera-pre-entrega-Novaro

Título: Tercera pre entrega
Fecha de entrega: 13 de Junio de 2023

Objetivos generales:
Desarrollar una Web Django con patrón MVT subida a GitHub.

Se debe entregar: 
Link de GitHub con el proyecto totalmente subido a la plataforma
Proyecto Web Django con patrón MVT que incluya:
	1- Herencia de HTML
	2- Por lo menos 3 clases de modelos
	3- Un formulario para insertar datos a todas las clases de tus modelos
	4- Un formulario para buscar algo en la base de datos
	5- Readme que indique el orden en que se prueban las cosas y/o donde están las funcionalidades
Formato:
Link al repositorio de GitHub con el nombre "Tercera pre-entrega+Apellido"

Funcionalidades del blog - Pasos resumidos: 
Clonar este repositorio en tu máquina local.
Abrir una termina en el proyecto original 
Instalar las dependencias del proyecto: pip install -r requirements.txt.
Ejecutar las migraciones: python manage.py migrate.
Ejecutar el servidor: python manage.py runserver.
Abrir en un navegador las siguientes urls:
- Administrador del blog: http://127.0.0.1:8000/admin.
- Página principal: http://127.0.0.1:8000/recetas/
- Crear recetas: http://127.0.0.1:8000/recetas/agregar_receta.
- Visualizar recetas: http://127.0.0.1:8000/recetas/recetas
- Crear datos de nutrición: http://127.0.0.1:8000/recetas/agregar_nutricion
- Visualizar datos de nutrición: http://127.0.0.1:8000/recetas/nutricion
- Crear datos de deportes: http://127.0.0.1:8000/recetas/agregar_deportes
- Visualizar datos de deportes: http://127.0.0.1:8000/recetas/deportes
- Buscar nutricionistas por su número de matrícula: Acceder a "Nutricion - Buscar Nutricionista por matrícula" y se redirigie al formulario en http://127.0.0.1:8000/busqueda_matricula.

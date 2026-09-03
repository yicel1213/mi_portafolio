from django.shortcuts import render
from datetime import datetime

def home(request):
    # Lógica para determinar el saludo según la hora actual
    hora_actual = datetime.now().hour
    if 6 <= hora_actual < 12:
        saludo = "¡Buenos días!"
    elif 12 <= hora_actual < 20:
        saludo = "¡Buenas tardes!"
    else:
        saludo = "¡Buenas noches!"

    context = {
        'saludo': saludo
    }
    return render(request, 'portfolio/home.html', context)

def projects(request):
    
    projects_list = [
        {"title": "Proyecto A", "description": "Desarrollo web con Django", "in_progress": True, "image": "img1.jpg"},
        {"title": "Proyecto B", "description": "Aplicación móvil con Flutter", "in_progress": False, "image": "img2.jpg"},
        {"title": "Proyecto C", "description": "Análisis de datos con Python", "in_progress": True, "image": "img3.jpg"},
    ]
    
    # Filtrar solo los proyectos que están en desarrollo (in_progress == True)
    filtered_projects = [p for p in projects_list if p['in_progress']]

    context = {
        'projects': filtered_projects
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    return render(request, 'portfolio/contact.html')
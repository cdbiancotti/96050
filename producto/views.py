from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

# def inicio(request):
#     return HttpResponse('<h1>HOLA BIENVENIDO A MI PAGINA!!</h1>')

def inicio(request):
    
    # v1
    # archivo_abierto = open(r'C:\Users\cdbia\Desktop\96050\django\producto\templates\inicio.html')
    # template = Template(archivo_abierto.read())
    # archivo_abierto.close()
    
    # with open(r'C:\Users\cdbia\Desktop\96050\django\producto\templates\inicio.html') as archivo_abierto:
    #     template = Template(archivo_abierto.read())
    
    # fecha_y_hora_actual = datetime.now()
    
    # contexto = Context({'fecha_y_hora_actual': fecha_y_hora_actual})
    
    # template_renderizado = template.render(contexto)
    
    # return HttpResponse(template_renderizado)

    # v2
    # template = loader.get_template('inicio.html')
    
    # fecha_y_hora_actual = datetime.now()
    
    # template_renderizado = template.render({'fecha_y_hora_actual': fecha_y_hora_actual})
    
    # return HttpResponse(template_renderizado)

    # 3
    fecha_y_hora_actual = datetime.now()
    
    # return render(request, 'inicio.html', {'fecha_y_hora_actual': fecha_y_hora_actual})
    return render(request, 'inicio_2.html', {'fecha_y_hora_actual': fecha_y_hora_actual})
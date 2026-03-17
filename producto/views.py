from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('hOLA BIENVENIDO A MI PAGIN!!')
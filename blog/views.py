from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template.response import TemplateResponse

def index(request):
    # return HttpResponse('Olá Django - index')
    return TemplateResponse(request, 'index.html', {})

def ola(request):
    return HttpResponse('Olá Django')

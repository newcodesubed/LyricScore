from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def app(request):
    template = loader.get_template('initial.html')
    return HttpResponse(template.render())

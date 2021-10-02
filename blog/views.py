from django.shortcuts import render
from django.views.generic import(View, TemplateView)
from . import models

# Create your views here.
class indexView(TemplateView):
    template_name = 'index.html'
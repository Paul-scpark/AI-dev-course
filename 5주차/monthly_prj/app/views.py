from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import pandas as pd
import csv

# Create your views here.
def index(request):
    return render(request, 'index.html')

def project_html(request):
    context = {}
    load_template = request.path.split('/')[-1]
    template = loader.get_template(load_template)
    return HttpResponse(template.render(context, request))

def get_data(request):
    return render(request, 'data_schema.html')

def get_data_eda(request):
    return render(request, 'data_eda.html')

def get_data_search(request):
    return render(request, 'data_search.html')

def get_community(request):
    return render(request, 'community.html')
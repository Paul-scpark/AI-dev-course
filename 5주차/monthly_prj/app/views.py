from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def project_html(request):
    context = {}
    load_template = request.path.split('/')[-1]
    print('@@@', load_template)
    template = loader.get_template(load_template)
    print('@@@', template)
    return HttpResponse(template.render(context, request))
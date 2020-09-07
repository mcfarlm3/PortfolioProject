from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project

# Create your views here.

def index(request):
    project_list = Project.objects.order_by('-created_date')[0:]
    template = loader.get_template('blog/index.html')
    context = {
        'project_list': project_list,
    }
    return HttpResponse(template.render(context,request))

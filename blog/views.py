from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project, Job

# Create your views here.

def index(request):
    project_list = Project.objects.order_by('-created_date')[0:]
    job_list = Job.objects.order_by('-end_year')[0:]
    template = loader.get_template('blog/index.html')
    context = {
        'project_list': project_list,
        'job_list': job_list,
    }
    return HttpResponse(template.render(context,request))

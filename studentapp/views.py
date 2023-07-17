from django.shortcuts import render
from django.http import HttpResponse
from studentapp.forms import StudentForm
from .models import Student
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
# Create your views here.


def student_info(request):
    return HttpResponse("Welcome")

class StudentCreateView(CreateView):
    # model = Student
    # fields =['name']
    form_class=StudentForm
    # model = Student
    # fields = ['']
    template_name='studentform.html'
    success_url='/studentcreate/'  








class CreateTemplate(TemplateView):
    template_name='studentcreate.html'


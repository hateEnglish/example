from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import *


def hello(req):
    context = dict()
    context["title"] = '12345678'
    return render(req, 'index.html', context)


def getOneStudent(req):
    stu = Student.objects.get(stu_name="张三")
    return HttpResponse(stu.stu_name)


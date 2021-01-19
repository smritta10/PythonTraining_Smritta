from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def func1(request):
    return HttpResponse("Hello, world. This is my First Django Assignment")

def template_func(request):
    context = {'tag var': "tag_var"}
    return render(request, "asg1.html", context)

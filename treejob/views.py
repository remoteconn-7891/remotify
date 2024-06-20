from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def trees(request):
    return HttpResponse('Hello World!')
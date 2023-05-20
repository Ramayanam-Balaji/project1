from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<marquee><h1>it is never late to dream</h1></marquee>')

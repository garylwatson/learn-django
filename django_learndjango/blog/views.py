from django.shortcuts import render
from django.http import HttpResponse #we added this

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
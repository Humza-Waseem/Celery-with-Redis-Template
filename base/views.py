
from django.shortcuts import render
from .tasks import fun
from django.http import HttpResponse

# Create your views here.

def testView(request):
    fun.delay()
    return HttpResponse(" Task has been completed")
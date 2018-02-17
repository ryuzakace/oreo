from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req,'base.html',{})

# Create your views here.

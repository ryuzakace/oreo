from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def home(req):
    return render(req,'home.html',{})

def test(req):
    return render(req,'test.html',{})
"""
def register(request):
    context = request.POST.get()
    print("This is context in views.py", context)
    if request.method =='POST':
        pass
    else:
        User_Form =  UserForm()
    return render(
            request,
            'registeration.html',
            context

            )
"""
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('basic:home')
    else:
        form = UserCreationForm()

    return render(
            request, 
            'register.html'
            ,{'form': form}
        )


from django.shortcuts import render
from django.http import HttpResponse
from .forms import DownloadForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .playlist import download_playlist


def home(req):
    return render(req,'home.html',{})

def test(req):
    return render(req,'test.html',{})

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email1')
            user = authenticate(username = username, email = email)
            login(request, user)
            return redirect('basic:download')
    else:
        form = UserCreationForm()

    return render(
            request, 
            'register.html'
            ,{'form': form}
        )

def dp(request):
    if request.method == 'POST':
        #form = DownloadForm(request.POST)
        ur = request.POST['url']
        download_playlist(ur)
        return render(request,'home.html',{})
    else:
        form = DownloadForm()

    return render(request,
                'download.html',
                {'form':form}
            )




def download(request):
    return render(
            request,
            'download.html',
            {}
        )







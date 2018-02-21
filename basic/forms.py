from django import forms
from django.contrib.auth.models import User

class regForm1(forms.Form):
    username = forms.CharField(label = 'handle', max_length = 50)
    email = forms.EmailField(label = 'email')


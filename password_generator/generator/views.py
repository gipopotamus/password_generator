from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    simbols = 'abcdefghijklmnopqrstuvwxyz'

    if request.GET.get('uppercase'):
        simbols += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if request.GET.get('special'):
        simbols += '!@#$%^&*()'

    if request.GET.get('numbers'):
        simbols += '0123456789'

    length = int(request.GET.get('length', 14))

    the_pass = ''.join(random.choices(simbols, k=length))

    return render(request, 'generator/home.html', {'pwd': the_pass})

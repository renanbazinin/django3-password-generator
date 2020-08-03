from django.http import HttpResponse
from django.shortcuts import render
import random

def home(request):
    return render(request,'generator/home.html',{'password':'1234'})


def password(request):



    chars = list('abcdefghjklmopqrstuvwyz')

    if request.GET.get('uppercase'):
        chars.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))
    if request.GET.get('spechar'):
        chars.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length'))

    thepassword = ''
    for x in range(length):
        thepassword+=random.choice(chars)

    return render(request,'generator/generator.html',{'password':thepassword})



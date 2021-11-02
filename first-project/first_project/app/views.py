import datetime
import os
from datetime import time
from os import listdir
from typing import Type

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'

    return HttpResponse(msg)


def workdir_view(request):
    current_dir = listdir('.')
    list_dir = f'Содержимое рабочего директория: {current_dir}'

    return HttpResponse(list_dir)

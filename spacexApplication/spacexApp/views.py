from datetime import date
import re
from django.shortcuts import render
from spacexApp.models import futureLaunch
import requests

def index(request):
    return render(request, 'spacexApp/index.html')

def launch_detail(request):
    launch_obj = futureLaunch.objects.all().order_by('id')
    return render(request, 'spacexApp/index.html', {'launch_obj': launch_obj})
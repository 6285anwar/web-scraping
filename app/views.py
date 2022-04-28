

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Create your views here.


def index(request):
    return render(request, 'user_index.html')

# ============ User Module ======================


def user_home(request):
    return render(request, 'user_home.html')


def user_ecommercescrap(request):
    return render(request, 'user_ecommercescrap.html')


def user_webscrap(request):
    return render(request, 'user_webscrap.html')


def user_listwebscrap(request):
    return render(request, 'user_listwebscrap.html')


def scrap(request):
    if request.method == "POST":
        vgm_url = request.POST['url']
        html_url = requests.get(vgm_url).text
        soup = BeautifulSoup(html_url, 'html.parser')
        print(soup.get_text())

        for link in soup.find_all(class_="_1YokD2 _3Mn1Gg"):
            print(link.get('h2'))

    return render(request, 'user_listwebscrap.html',{'link':link})

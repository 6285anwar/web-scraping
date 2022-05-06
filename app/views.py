from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime,date,timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
import requests
from bs4 import BeautifulSoup


# Create your views here.


def login(request):
    if request.method == 'POST':
        username  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect( 'admin_home')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            users=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['u_id'] = users
            request.session['username'] = users.fullname
            request.session['u_id'] = users.id 
            users=user_registration.objects.filter(id= users.id)          
            return render(request,'user_home.html',{'users':users})
    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        u=user_registration()
        u.fullname = request.POST['name']
        u.username = request.POST['username']
        u.email = request.POST['email']
        u.password = request.POST['password']
        u.photo = request.FILES['photo']
        u.joiningdate = datetime.now()
        
        u.save()
        
        return render(request, 'login.html')

    return render(request, 'register.html')

# ============ Admin Module ======================
def admin_logout(request):
    if 'Adm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
            


def admin_index(request):
    return render(request, 'admin_index.html')
def admin_home(request):
    user=user_registration.objects.count()
   
    return render(request, 'admin_home.html',{'user':user})

def admin_user(request):
    user=user_registration.objects.all()
    return render(request, 'admin_user.html',{'user':user})

def admin_user_delete(request, id):
    user = user_registration.objects.get(id=id)
    user.delete()
    return redirect('admin_user')





# ============ User Module ======================
def user_logout(request):
    if 'u_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def user_index(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']
 
    users = user_registration.objects.filter(id=u_id)
    return render(request, 'user_index.html',{'users':users})

def user_home(request):
    return render(request, 'user_home.html')


def user_ecommercescrap(request):
    return render(request, 'user_ecommercescrap.html')


# def user_webscrap(request):
#     return render(request, 'user_webscrap.html')


def user_listwebscrap(request):
    return render(request, 'user_listwebscrap.html')
def user_imbd(request):
    return render(request, 'user_imbd.html')

def scrap(request):
    if request.method == "POST":
        vgm_url = request.POST['url']
        html_url = requests.get(vgm_url).text
        soup = BeautifulSoup(html_url, 'html.parser')
        print(soup.get_text())

        for link in soup.find_all(class_="_1YokD2 _3Mn1Gg"):
            print(link.get('h2'))

    return render(request, 'user_listwebscrap.html', {'link': link})


def view(request):
    full_name = []
    full_price = []
    full_rate = []
    full_url = []

    file_name = "{}data.csv".format(settings.STATIC_URL)
    file = open(file_name, 'w')
    header = 'Name,Price,Rate,Url\n'
    file.write(header)

    if request.method == "POST":
        url = request.POST['url']
        if 'https://' not in url:
            messages.error(request, "Error")
        else:
            page_url = requests.get(url)
            pagesoup = soup(page_url.text, 'html.parser')

            main_class = pagesoup.find_all('div', {'class': '_1UoZlX'})

            for i in main_class:
                pdt_name = i.find('div', {'class': '_3wU53n'}).text.replace(
                    ',', '').replace('\r', '').replace('\n', '')
                pdt_price = i.find('div', {'class': '_1vC4OE _2rQ-NK'}).text.replace(
                    ',', '').replace('\r', '').replace('\n', '')
                pdt_rate = i.find('div', {'class': 'hGSR34'}).text.replace(
                    ',', '').replace('\r', '').replace('\n', '')
                pdt_url = i.find('a', {'class': '_31qSD5'})['href']
                pdt_main_url = 'https://www.flipkart.com'+pdt_url

                full_name.append(pdt_name)
                full_price.append(pdt_price)
                full_rate.append(pdt_rate)
                full_url.append(pdt_main_url)

                file.write(pdt_name+','+str(pdt_price)+',' +
                           pdt_rate+','+pdt_main_url+'\n')

        mylist = zip(full_name, full_price, full_rate, full_url)
        file.close()
        return render(request, 'user_webscrap.html', {'mylist': mylist})
    return render(request, 'user_webscrap.html')


def user_webscrap(request):
    if request.method == "POST":
        url = request.POST['url']

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find('table',  {'class': 'chart full-width'})
        rows = table.find_all('tr')
        movies = []
        for row in rows:
            image = row.find('img')
            if image:
                movies.append(image['alt'])
        return render(request, "user_webscrap.html", {'movies': movies})



def user_escrap(request):
    return render(request, "user_escrap.html")
    
def user_eview(request):
    if request.method == "POST":
        url = request.POST['url']

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find('div',  {'class': '_1YokD2 _3Mn1Gg'})
        rows = table.find_all('div',  {'class': '_4rR01T'}) 
        movies = []
        for row in rows:
            image = row.find('img')
            if image:
                movies.append(image['alt'])
        return render(request, "user_eview.html", {'movies': movies})

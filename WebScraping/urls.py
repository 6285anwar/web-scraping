"""WebScraping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^index/$', views.index,name='index'),

#============ User Module ======================

    re_path(r'^$', views.user_home, name='user_home'),
    re_path(r'^user_webscrap/$', views.user_webscrap, name='user_webscrap'),
    re_path(r'^user_listwebscrap/$', views.user_listwebscrap, name='user_listwebscrap'),
    re_path(r'^user_ecommercescrap/$', views.user_ecommercescrap, name='user_ecommercescrap'),
    re_path(r'^scrap/$', views.scrap, name='scrap')


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
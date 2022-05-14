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
    re_path(r'^$', views.login,name='login'),
    re_path(r'^register$', views.register,name='register'),


#============ Admin Module ======================
    re_path(r'^admin_logout/$', views.admin_logout,name='admin_logout'),
    re_path(r'^admin_index/$', views.admin_index,name='admin_index'),
    re_path(r'^admin_home/$', views.admin_home,name='admin_home'),
    re_path(r'^admin_user/$', views.admin_user,name='admin_user'),
    re_path(r'^admin_userscraphistory/$', views.admin_userscraphistory,name='admin_userscraphistory'),

    re_path(r'^admin_user_delete/(?P<id>\d+)/$', views.admin_user_delete,name='admin_user_delete'),
    re_path(r'^admin_datas/$', views.admin_datas,name='admin_datas'),
    re_path(r'^admin_data_add/$', views.admin_data_add,name='admin_data_add'),
    re_path(r'^admin_viewdata/(?P<id>\d+)/$', views.admin_viewdata, name='admin_viewdata'),

    re_path(r'^admin_editviewdata/(?P<id>\d+)/$', views.admin_editviewdata, name='admin_editviewdata'),
    re_path(r'^admin_deletedata/(?P<id>\d+)/$', views.admin_deletedata,name='admin_deletedata'),











#============ User Module ======================
    re_path(r'^user_logout/$', views.user_logout,name='user_logout'),

    re_path(r'^user_index/$', views.user_index, name='user_index'),
    
    re_path(r'^user_home/$', views.user_home, name='user_home'),
    re_path(r'^user_scrapsite/$', views.user_scrapsite, name='user_scrapsite'),
    re_path(r'^user_scrapsitedata/$', views.user_scrapsitedata, name='user_scrapsitedata'),

    re_path(r'^user_viewdata/$', views.user_viewdata, name='user_viewdata'),
    re_path(r'^user_datascrap/$', views.user_datascrap,name='user_datascrap'),



    re_path(r'^user_webscrap/$', views.user_webscrap, name='user_webscrap'),
    re_path(r'^user_listwebscrap/$', views.user_listwebscrap, name='user_listwebscrap'),
    re_path(r'^user_ecommercescrap/$', views.user_ecommercescrap, name='user_ecommercescrap'),
    re_path(r'^user_imbd/$', views.user_imbd, name='user_imbd'),
    re_path(r'^scrap/$', views.scrap, name='scrap'),
    re_path(r'^view/$',views.view,name='view'),
    re_path(r'^user_escrap/$', views.user_escrap, name='user_escrap'),
    re_path(r'^user_eview/$', views.user_eview, name='user_eview'),

    re_path(r'^user_scrapword/$', views.user_scrapword, name='user_scrapword'),
    re_path(r'^user_error/$', views.user_error, name='user_error'),
    re_path(r'^user_scrapitem/$', views.user_scrapitem, name='user_scrapitem'),




]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
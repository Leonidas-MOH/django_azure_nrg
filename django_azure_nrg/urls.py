"""django_azure_nrg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path , include
from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout




from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView,
)

import django.contrib.auth.urls

#from countries import views

##urlpatterns = [
##    path('admin/', admin.site.urls),
##    path('admin0/', admin.site.urls,   name='password_change' ),
##    path('country', Home, name='country-home'),
##]

def MainMenu(request):
    return render(request, 'NewMenuBootStrap.html')


#url(r'^sign-out/$', logout, {'template_name': 'index.html', 'next_page': '/'}, name='sign-out'),

urlpatterns = [
    path('', MainMenu , name='MainMenu'),    
    path('menu/', MainMenu , name='MainMenu'),
    path('accounts/', include('django.contrib.auth.urls')),
#    url(r'^menu1/', views.NewMenu1),

##    #url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls , name=admin),
##    url(r'^login/$', login, name='login'),
##    url(r'^logout/$', logout, name='logout'),
##
##?next=/admin/
    
##    url(r'^password_change/$', PasswordChangeView, name='password_change'),
##    url(r'^password_change/done/$', PasswordChangeDoneView, name='password_change_done'),
##    url(r'^password_reset/$', PasswordResetView, name='password_reset'),
##    url(r'^password_reset/done/$', PasswordResetDoneView, name='password_reset_done'),
##    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
##        PasswordResetConfirmView, name='password_reset_confirm'),
##    url(r'^reset/done/$', PasswordResetCompleteView, name='password_reset_complete'),
##    #url(r'^admin/', admin.site.urls),

    url(r'^country/', include(('countries.urls', "country") , namespace="country")),
    url(r'^metric/', include(('metrics.urls', "metric") , namespace="metric")),
    url(r'^fetchparams/', include(('fetchparams.urls', "fetchparams") , namespace="fetchparams")),    
    url(r'^scheduler/', include(('scheduler.urls', "scheduler") , namespace="scheduler")),
    url(r'^datapool/', include(('datapool.urls', "datapool") , namespace="datapool")),        
    #url(r'^Meteologica/', include('meteologica.urls', namespace="meteologica")),

#    path('count', views.Home, name='country-home'),

#    url(r'', views.MainMenu, name='MainMenu'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

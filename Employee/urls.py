"""
URL configuration for core project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from Employee.views import *
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('homepageE/', views.homePage,name='homePageE'),
    path('aboutusE/', views.aboute, name='aboutusE'),
    path('bookingE/', views.booking_details, name='bookingDetails'),
    path('bookingvE/', views.booking_verify, name='bookingvE'),
    path('loginE/', views.logine, name='insertlogin'),
    path('insertloginE/', views.insertLogin, name='insertlogin'),
    path('registrationE/', views.registratione, name='registrationE'),
    #  path('registratione/', views.registratione, name='registratione'),
    
]

urlpatterns += staticfiles_urlpatterns()
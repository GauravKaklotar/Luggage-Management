"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
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
from django.contrib import admin
from django.urls import path,include
from MainProject.views import *
from Employee.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MainProject.urls')),
    path('',include('Employee.urls')),
    path('',include('Admin.urls'))
    # path('aboutus/', aboutus, name='aboutus'),
    # path('booking/', booking, name='booking'),
    # path('contactus/', contactus, name='contactus'),
    # path('login/', login, name='login'),
    # path('registration/', registration, name='registration'),
]
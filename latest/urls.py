"""latest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from latestapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relatedpage/',views.drug_abuse),
    path('site/',views.loginpage),
    #path('login/',views.signin),
    #path('signup/',views.signup),
    path('login/', views.login),
    #path('reg/', views.register),
   # path('hellooo/',views.hello),
    path('linkpage/', views.signup),
    path('legal/', views.signuplegalofficer),
    path('narcotic/', views.signupnarcotic),
    path('medical/', views.signupmedical),
    path('customs/', views.signupcustoms),
    path('socialworker/', views.signupsocialworker),
    path('index/', views.index),
    path('logout/', views.logout),
    path('drugabuse/', views.drug_abuse),
    path('E1/', views.events),
    path('E2/', views.event1),
    path('E3/', views.event2),
    path('delete/', views.remove),
    path('retrive/', views.retrive),
    path('update/', views.update),
    path('ss/', views.ss),

   # path('forlogin/', views.forlogin),
    path('forcontact/', views.forcontact),
    path('infographics/', views.infographics),
    path('commondrugs/', views.commondrugs),
    path(' about/', views.about),
    #path(' legalhome/', views. legalhome),

    #path(' legalforvictims/', views.legalforvictims),



]

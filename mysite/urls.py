"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.shortcuts import render
from .views import CustomersView, OrdersView, PingView, ProductView
import requests
import json


def landingPage(request):
    print()
    product = getInfo(request.get_port())
    print(product)
    return render(request, 'index.html', {"product": product})


def getInfo(rooturl):
#     url = "http://127.0.0.1:" + rooturl + "/product"
    url = "http://0.0.0.0:10000/product"
    api_call = requests.get(url, headers={})
    return json.loads(api_call.content)


urlpatterns = [
    path('', landingPage, name='landing'),
    path('admin/', admin.site.urls),

    path('ping/', PingView.as_view()),

    # Endpoints for customers URL.
    path('customer/', CustomersView.as_view(), name='customers'),
    path('customer/<uuid:id>/', CustomersView.as_view(), name='customers'),

    # Endpoints for customers URL.
    path('product/', ProductView.as_view(), name='product'),
    path('product/<uuid:id>/', ProductView.as_view(), name='product'),

    path('order/', OrdersView.as_view(), name='order'),
]

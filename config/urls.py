"""config URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from demos.views import home

#from demos.views import lotto, home, input
urlpatterns = [
    #path('', home, name='home'), 
    path('admin/', admin.site.urls),
    # path('init', input, name='input'),
    # path('init/lotto', lotto, name='result'),
    #프로젝트 내 앱이 여러개일 때 url분기 처리:
    path('demos/', include('demos.urls')),
    path('customer_services/', include('customer_services.urls')),
]

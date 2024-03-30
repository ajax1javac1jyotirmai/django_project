"""
URL configuration for techassignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from .views import client_detail, client_list,  create_projectiii, project_list,project_detail
#,include
# from django.conf.urls import url
# from .views import client_list, client_detail, project_create, project_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', client_list),
   
     path('projects/', project_list),
   
     path('projects/<int:pk>/',project_detail),
   
    path('clients/<int:pk>/',client_detail),
  
    path('createpro/',create_projectiii)
  
  
  
   
    
  
   
  
]


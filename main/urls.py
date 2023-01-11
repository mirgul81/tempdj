"""temlate_django URL Configuration

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
    TEST
"""
from django.urls import path, include
from .views import (
    indexView,
    sverdlovView,
    batkenView,
    create_regionView,
    create_areaView,
    update_regionView,
    delete_regionView,
    update_areaView,
    delete_areaView,

)

app_name = 'main'


urlpatterns = [

    path('index/', indexView, name= 'index'),
    path('sverdlov/<int:pk>/',  sverdlovView, name='sverdlov'),
    path('create_region/', create_regionView, name='create_region'),
    path('batken/<int:pk>/', batkenView, name='batken'),
    path('create_area/', create_areaView, name='create_area'),
    path('update_region/<int:id>/',update_regionView, name='update_region'),
    path('delete_region/<int:id>/',delete_regionView, name='delete_region'),
    path('update_area/<int:id>/',update_areaView, name='update_area'),
    path('delete_area/<int:id>/',delete_areaView, name='delete_area')
]

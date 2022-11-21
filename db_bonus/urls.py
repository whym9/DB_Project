"""db_bonus URL Configuration

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
from django.urls import path
from medical_service import views  
from db_bonus import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('', views.main_view),
    path('admin/', admin.site.urls), 
    path('country', views.countr),   
    path('diseaseType', views.diseaseType),
    path('country_view',views.country_view),  
    path('country_edit/<str:cname>', views.country_edit),  
    path('country_update/<str:cname>', views.country_update),  
    path('country_delete/<str:cname>', views.country_delete), 

    path('diseaseType_view',views.diseaseT_view), 
    path('diseaseType_edit/<int:id>', views.diseaseT_edit),  
    path('diseaseType_update/<int:id>', views.diseaseT_update),  
    path('diseaseType_delete/<int:id>', views.diseaseT_delete),
    
    path('disease', views.disease),
    path('disease_view',views.disease_view), 
    path('disease_edit/<str:code>', views.disease_edit),  
    path('disease_update/<str:code>', views.disease_update),  
    path('disease_delete/<str:code>', views.disease_delete),

    path('discover', views.discover),
    path('discover_view',views.discover_view), 
    path('discover_edit/<str:cname>,<str:code>', views.discover_edit),  
    path('discover_update/<str:cname>,<str:code>', views.discover_update),  
    path('discover_delete/<str:cname>,<str:code>', views.discover_delete),

    path('users', views.users),
    path('users_view',views.users_view), 
    path('users_edit/<str:email>', views.users_edit),  
    path('users_update/<str:email>', views.users_update),  
    path('users_delete/<str:email>', views.users_delete),

    path('public', views.public),
    path('public_view',views.public_view), 
    path('public_edit/<str:email>', views.public_edit),  
    path('public_update/<str:email>', views.public_update),  
    path('public_delete/<str:email>', views.public_delete),

    path('doctor', views.doctor),
    path('doctor_view',views.doctor_view), 
    path('doctor_edit/<str:email>', views.doctor_edit),  
    path('doctor_update/<str:email>', views.doctor_update),  
    path('doctor_delete/<str:email>', views.doctor_delete),

    path('spec', views.spec),
    path('spec_view',views.spec_view), 
    path('spec_edit/<str:id>,<str:email>', views.spec_edit),  
    path('spec_update/<str:id>,<str:email>', views.spec_update),  
    path('spec_delete/<str:id>,<str:email>', views.spec_delete),

    path('record', views.record),
    path('record_view',views.record_view), 
    path('record_edit/<str:email>,<str:cname>,<str:code>', views.record_edit),  
    path('record_update/<str:email>,<str:cname>,<str:code>', views.record_update),  
    path('record_delete/<str:email>,<str:cname>,<str:code>', views.record_delete),
]  



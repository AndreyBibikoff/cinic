"""clinic URL Configuration

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
from django.urls import path, include

from patient.views import patients, add_patient, patient_detail, opd, dogovor2str, ids_opd, el_boln, med_card, \
    dogovor5str, ids

app_name = 'patient'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', patients, name='patients'),
    path('add_patient/', add_patient, name='add_patient'),
    path('patient_detail/<int:pk>/', patient_detail, name='patient_detail'),
    path('opd/<int:pk>/', opd, name='opd'),
    path('dogovor5str/<int:pk>/', dogovor5str, name='dogovor5str'),
    path('old_dogovor2str/<int:pk>/', dogovor2str, name='dogovor2str'),
    path('ids_opd/<int:pk>/', ids_opd, name='ids_opd'),
    path('ids/<int:pk>/', ids, name='ids'),
    path('soglasie_na_boln/<int:pk>/', el_boln, name='el_boln'),
    path('med_card/<int:pk>/', med_card, name='med_card'),

]

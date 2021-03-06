"""conf URL Configuration

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
from django.contrib import admin
from django.urls import path
from python_junior_jobs.views import main_view, companies_view, vacancy_view, exit_view, vacancies_view, specialty_view, all_vacancies_view
from python_junior_jobs.views import custom_handler400, custom_handler403, custom_handler404, custom_handler500


handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('', main_view, name='main'),
    path('vacancies', vacancies_view, name='vacancies'),
    path('specialty/<str:vacancies_1>/<str:vacancies_2>', specialty_view, name='specialty'),
    path('companies/<int:id>', companies_view, name='companies'),
    path('vacancy/<int:id>', vacancy_view, name='vacancy'),
        path('allvacancies', all_vacancies_view, name='all_vacancies'),
    path('exit', exit_view, name='exit'),
    path('admin/', admin.site.urls),
]

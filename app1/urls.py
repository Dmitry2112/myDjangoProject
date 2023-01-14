from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('demand', views.demand, name='demand'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('latest-vacancies', views.latest_vacancies, name='latest_vacancies')
]
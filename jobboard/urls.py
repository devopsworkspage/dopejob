from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs_list', views.index, name='jobs_list'),
]

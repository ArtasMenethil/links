from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('links', views.create_and_list, name='links'),
    path('who_are_we', views.who_are_we, name='who_are_we'),
]

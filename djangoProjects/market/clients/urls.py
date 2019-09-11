from django.urls import path

from.import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('', views.hi, name='hi'),
    path ('', views.list_Clients, name='list_Clients'),
]
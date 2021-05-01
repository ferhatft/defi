from django.urls import path, include
from .views import bilgi, Addbilgi, bilgidetay, infromation_update, infromation_delete

urlpatterns = [
    path('', bilgi, name="bilgi"),
    path('read/<slug:slug>/', bilgidetay, name="bilgidetay"),
    path('add/', Addbilgi, name="addbilgi"),
    path('update/<slug:slug>/', infromation_update, name="infromation_update"),
    path('delete/<slug:slug>/', infromation_delete, name="infromation_delete"),


    path('tag/<slug:slug>/', bilgi, name="taginfolist"),

]

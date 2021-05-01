from django.urls import path, include
from .views import  news,newsdetay,Addnews,new_update,new_delete

urlpatterns = [
    path('', news, name="news"),
    path('read/<slug:slug>/', newsdetay, name="newsdetay"),
    path('add/', Addnews, name="addnews"),
    path('update/<slug:slug>/', new_update, name="new_update"),
    path('delete/<slug:slug>/', new_delete, name="new_delete"),


    # path('tag/<slug:slug>/', bilgi, name="taginfolist"),

]

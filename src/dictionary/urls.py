from django.urls import path, include

from dictionary.views import dictionary,all_dictionary,dictionarydetail,dictionary_update,dictionary_delete,dictionary_create,dictionary_report,dic_upwote,dic_dawnvote


urlpatterns = [
    path('', dictionary, name="dictionary"),
    path('all/', all_dictionary, name="all_dictionary"),
    
    path('detail/<str:cats>/', dictionarydetail, name= "dictionarydetail"),
    
    path('update/<slug:slug>/', dictionary_update, name= "dictionary_update"),
    path('delete/<slug:slug>/', dictionary_delete, name= "dictionary_delete"),
    
    path('report/<slug:slug>/', dictionary_report, name= "dictionary_report"),
    path('dictionary-create/', dictionary_create, name= "dictionary_create"),
    path('tag/<slug:tag_slug>/', dictionary, name= "taglist"),
    
    path('upvote/<int:id>/', dic_upwote , name= "dic_upwote"),
    path('dawnvote/<int:id>/', dic_dawnvote , name= "dic_dawnvote"),

]
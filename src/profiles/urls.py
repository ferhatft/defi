
from django.urls import include, path
from profiles import views

urlpatterns = [
    path('', views.Userprofile, name="Userprofile"),
    
    path('update/', views.UpdateUserprofile, name= "UpdateUserprofile"),
]

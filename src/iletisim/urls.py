
from django.urls import path

from .views import contacview


app_name = 'iletisim'

urlpatterns = [
    path('' , contacview, name="iletisim"),
   
]


from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views



urlpatterns = [
    path('', views.index,name='index'),
    
    
    
]
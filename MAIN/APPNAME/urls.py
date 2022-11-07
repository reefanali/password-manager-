from django.urls import path
###3from .views import home###
from . import views

urlpatterns = [
    ###path("", home, name="home"),
    path('',views.home, name='home'),
    path('password',views.password, name='password')
] 
from django.urls import path
from . import views

app_name = 'face'

urlpatterns = [
    path('', views.addUser, name='home'),
]

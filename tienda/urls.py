from django.urls import path
from . import views

urlpatterns = [
    path('productos', views.list_productos),
    path('', views.index, name='index'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tabla2/', views.list_view, name='lista2'),
]
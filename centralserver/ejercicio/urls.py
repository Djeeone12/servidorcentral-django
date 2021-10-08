from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tabla2/', views.list_view, name='lista2'),
    path('poke1/', views.poke_get, name='poke1'),
    path('poke2/', views.poke_post, name='poke2'),
    path('poke3/', views.poke_put, name='poke3'),
    path('poke4/', views.poke_delete, name='poke4'),
]
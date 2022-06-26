from django.urls import path
from . import views

app_name = 'specialties'

urlpatterns = [
    path('', views.list_specialties, name='list_specialties'),
    path('adicionar/', views.add_specialty, name='add_specialty'),
    path('editar/<int:id_specialty>/', views.edit_specialty, name='edit_specialty'),
    path('excluir/<int:id_specialty>/', views.delete_specialty, name='delete_specialty'),
]
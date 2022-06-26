from django.urls import path
from . import views

app_name = 'exams'

urlpatterns = [
    path('', views.list_exams, name='list_exams'),
    path('adicionar/', views.add_exam, name='add_exam'),
    path('editar/<int:id_exam>/', views.edit_exam, name='edit_exam'),
    path('excluir/<int:id_exam>/', views.delete_exam, name='delete_exam'),
]
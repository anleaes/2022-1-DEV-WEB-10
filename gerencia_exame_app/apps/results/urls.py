from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('', views.list_results, name='list_results'),
    path('adicionar/<int:id_patient>/', views.add_result, name='add_result'),
    path('excluir/<int:id_result>/', views.delete_result, name='delete_result'),
    path('excluir-item/<int:id_result_item>/', views.delete_result_item, name='delete_result_item'),
    path('adicionar-item/<int:id_result>/', views.add_result_item, name='add_result_item'),
    path('editar-status/<int:id_result>/', views.edit_result_status, name='edit_result_status'),
]
from django.urls import path

from enterprise import views

urlpatterns = [
    path ('nova_empresa/', views.new_enterprise, name="new_enterprise"),
    path('empresas/', views.show_enterprises, name="show_enterprises"),
    path('excluir_empresa/<int:id>', views.delete_enterprise, name="delete_enterprise"),
]

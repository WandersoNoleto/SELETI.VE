from django.urls import path

from companys import views

urlpatterns = [
    path ('nova_empresa/', views.new_companys, name="new_company"),
    path('empresas/', views.show_companys, name="show_companys"),
    path('excluir_empresa/<int:id>', views.delete_companys, name="delete_company"),
]

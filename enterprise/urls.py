from django.urls import path

from enterprise import views

urlpatterns = [
    path ('nova_empresa/', views.new_enterprise, name="new_enterprise")
]

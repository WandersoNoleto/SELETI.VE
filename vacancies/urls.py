from django.urls import path

from vacancies import views

urlpatterns = [
    path('nova-vaga/', views.new_vacancy, name="new_vacancy" )
]

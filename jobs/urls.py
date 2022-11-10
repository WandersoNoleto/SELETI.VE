from django.urls import path

from jobs import views

urlpatterns = [
    path('nova-vaga/', views.new_job, name="new_job")
]

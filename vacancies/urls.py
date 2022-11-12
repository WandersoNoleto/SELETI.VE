from django.urls import path

from vacancies import views

urlpatterns = [
    path('nova-vaga/', views.new_vacancy, name="new_vacancy" ),
    path('vaga/<int:id>', views.show_vacancy, name="show_vacancy"),
    path('nova-tarefa/<int:id_vacancy>', views.new_task, name="new_task"),
    path('realizar_tarefa/<int:id>', views.finish_task, name='finish_task'),
    path('envia-email/<int:id_vacancy>', views.send_email, name="send_email")
]

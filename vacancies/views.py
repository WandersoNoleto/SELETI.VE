from django.conf import settings
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import EmailMultiAlternatives
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from companys.models import Vacancy
from vacancies.models import Emails, Task


def new_vacancy(request):
    if request.method == "POST":
        title = request.POST.get('title')
        email = request.POST.get('email')
        technologies_mastered = request.POST.get('technologies_mastered')
        technologies_to_study = request.POST.get('technologies_to_study')
        experience = request.POST.get('experience')
        final_date = request.POST.get('final_date')
        company = request.POST.get('company')
        status = request.POST.get('status')


        vacancy = Vacancy(
                    title=title,
                    email=email,
                    lvl_experience=experience,
                    final_date=final_date,
                    company_id=company,
                    status=status,
        )


        vacancy.save() 

        vacancy.technologies_to_study.add(*technologies_to_study)
        vacancy.technologies_matereds.add(*technologies_mastered)

        vacancy.save()

        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/home/empresa/{company}')
    elif request.method == "GET":
        raise Http404()

def show_vacancy(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    tasks = Task.objects.filter(vacancy=vacancy).filter(concluded=False)
    emails = Emails.objects.filter(vacancy=vacancy)
    
    context = {
        'vacancy': vacancy,
        'tasks': tasks,
        'email': emails
    }

    return render(request, 'vacancy_details.html', context)

def new_task(request, id_vacancy):
    title = request.POST.get('title')
    priority = request.POST.get('priority')
    date = request.POST.get('date')
    
    task = Task(vacancy_id=id_vacancy,
                    title=title,
                    priority=priority,
                    date=date)
    task.save()
    messages.add_message(request, constants.SUCCESS, 'Tarefa criada com sucesso')
   
    return redirect(f'/vagas/vaga/{id_vacancy}')

def finish_task(request, id):
    task_list = Task.objects.filter(id=id).filter(concluded=False)

    if not task_list.exists():
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect(f'/home/empresas/')

    task = task_list.first()
    task.concluded = True
    task.save()    
    messages.add_message(request, constants.SUCCESS, 'Tarefa realizada com sucesso, parabéns!')
    return redirect(f'/vagas/vaga/{task.vacancy.id}')

def send_email(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    title = request.POST.get('title')
    main_text = request.POST.get('main_text')

    html_content = render_to_string('emails/template_email.html', {'main_text': main_text})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(title, text_content, settings.EMAIL_HOST_USER, [vacancy.email,])
    email.attach_alternative(html_content, "text/html")

    if email.send():  
        email_to_save = Emails(
            vacancy=vacancy,
            title=title,
            main_text=main_text,
            sent=True
        )

        email_to_save.save()

        messages.add_message(request, constants.SUCCESS, 'Email enviado com sucesso.')
        return redirect(f'/vagas/vaga/{vacancy_id}')
    else:
        email_to_save = Emails(
            vacancy=vacancy,
            title=title,
            main_text=main_text,
            sent=False
        )

        email_to_save.save()

        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect(f'/vagas/vaga/{vacancy_id}')
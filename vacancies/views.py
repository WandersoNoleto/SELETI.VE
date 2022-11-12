from django.contrib import messages
from django.contrib.messages import constants
from django.http import Http404
from django.shortcuts import redirect, render

from companys.models import Vacancy


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
    elif request.method == "GET":
        raise Http404()
from django.contrib import messages
from django.contrib.messages import constants
from django.http import Http404
from django.shortcuts import redirect

from companys.models import Jobs


def new_job(request):
    if request.method == "POST":
        title = request.POST.get('title')
        email = request.POST.get('email')
        technologies_mastered = request.POST.get('technologies_master')
        technologies_to_study  = request.POST.get('technologies_study')
        experience = request.POST.get('experience')
        final_date = request.POST.get('final_date')
        company = request.POST.get('company')
        status = request.POST.get('status')

        jobs = Jobs (
            title = title,
            email = email,
            lvl_experience = experience,
            final_date = final_date,
            company_id=company,
            status=status
        )

        jobs.save()

        jobs.technology_study.add(*technologies_to_study)
        jobs.technologies_master.add(*technologies_mastered)

        jobs.save()

        messages.add_message(request, constants.SUCCESS, 'Vaga criada com sucesso.')
        return redirect(f'/home/empresa/{company}')
    elif request.method == "GET":
        raise Http404()


from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect, render

from companys.models import Company, Technology


def new_companys(request):

    if request.method == "GET":
        techs = Technology.objects.all()
        
        context = {
            "techs": techs
        }

        return render(request, 'new_company.html', context)
        
    elif request.method == "POST":
        name  = request.POST.get('name')
        email = request.POST.get('email')
        city  = request.POST.get('city')
        address  = request.POST.get('address')
        category = request.POST.get('category')
        characteristics = request.POST.get('characteristics')
        technologies = request.POST.getlist('technologies')
        logo = request.FILES.get('logo')

        if (len(name.strip()) == 0 or len(email.strip()) == 0 or len(city.strip()) == 0 or len(address.strip()) == 0 or len(category.strip()) == 0 or len(characteristics.strip()) == 0 or (not logo)): 
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'A logo da empresa deve ter menos de 10MB')
            return redirect('/home/nova_empresa')

        if category not in [i[0] for i in companys.choices_category]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/home/nova_empresa')

        companys = companys(logo=logo,
                        name=name,
                        email=email,
                        city=city,
                        address=address,
                        market_category=category,
                        company_characteristics=characteristics
                    )

        companys.save()
        companys.technology.add(*technologies)
        companys.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        return redirect('/home/empresas')

def show_companys(request):
    companys  = Company.objects.all()
    technologies = Technology.objects.all()

    tech_filter = request.GET.get('technologies')
    name_filter = request.GET.get('name')

    if tech_filter:
        companys = companys.filter(technology = tech_filter)

    if name_filter:
       companys = companys.filter(name__icontains = name_filter)

    context = {
        "companys":  companys,
        "technologies": technologies
    }

    return render(request, 'companys.html', context)

def delete_companys(request, id):
    companys = Company.objects.get(id=id)
    companys.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
    return redirect('/home/empresas')

def company_details(request, id):
    company = get_object_or_404(Company, id=id)

    context = {
        'company': company
    }

    return render(request, 'company.html', context)

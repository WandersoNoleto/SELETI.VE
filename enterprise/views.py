from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from enterprise.models import Enterprise, Technology


def new_enterprise(request):

    if request.method == "GET":
        techs = Technology.objects.all()
        
        context = {
            "techs": techs
        }

        return render(request, 'new_enterprise.html', context)
        
    elif request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        address = request.POST.get('address')
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

        if category not in [i[0] for i in Enterprise.choices_category]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect('/home/nova_empresa')

        enterprise = Enterprise(logo=logo,
                        name=name,
                        email=email,
                        city=city,
                        address=address,
                        market_category=category,
                        company_characteristics=characteristics
                    )

        enterprise.save()
        enterprise.technology.add(*technologies)
        enterprise.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        return redirect('/home/empresas')
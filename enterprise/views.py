from django.http import HttpResponse
from django.shortcuts import render


def new_enterprise(request):
    return render(request, 'new_enterprise.html')
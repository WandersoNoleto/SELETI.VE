from django.contrib import admin

from companys.models import Company, Technology, Vacancy

admin.site.register(Technology)
admin.site.register(Company)
admin.site.register(Vacancy)
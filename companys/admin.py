from django.contrib import admin

from companys.models import Company, Jobs, Technology

admin.site.register(Technology)
admin.site.register(Company)
admin.site.register(Jobs)
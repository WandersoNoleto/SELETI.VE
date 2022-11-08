from django.contrib import admin

from enterprise.models import Enterprise, Jobs, Technology

admin.site.register(Technology)
admin.site.register(Enterprise)
admin.site.register(Jobs)
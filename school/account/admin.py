from django.contrib import admin
from .models import Invite, CsvFile


class InviteAdmin(admin.ModelAdmin):
    list_display = ['email', 'sent_date']


class CsvFileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


admin.site.register(Invite, InviteAdmin)
admin.site.register(CsvFile, CsvFileAdmin)
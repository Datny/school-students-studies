from django.contrib import admin
from .models import Invite


class InviteAdmin(admin.ModelAdmin):
    list_display = ['email', 'sent_date']


admin.site.register(Invite, InviteAdmin)

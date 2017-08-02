# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Mitglied, Dienst, Dienstgebiet, Dienstart, Fahrzeug


class ProfileInline(admin.StackedInline):
    model = Mitglied
    can_delete = False
    verbose_name_plural = 'Mitglied'
    # fk_name = 'user'


class MitgliedUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(MitgliedUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)

admin.site.register(User, MitgliedUserAdmin)
admin.site.register(Dienstart)
admin.site.register(Dienstgebiet)
admin.site.register(Dienst)
admin.site.register(Fahrzeug)

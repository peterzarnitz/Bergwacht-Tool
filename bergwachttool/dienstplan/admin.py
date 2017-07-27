# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Nutzer, Dienst, Dienstgebiet, Dienstart


class ProfileInline(admin.StackedInline):
    model = Nutzer
    can_delete = False
    verbose_name_plural = 'Nutzer'
    # fk_name = 'user'


class NutzerUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(NutzerUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)

admin.site.register(User, NutzerUserAdmin)
admin.site.register(Dienstart)
admin.site.register(Dienstgebiet)
admin.site.register(Dienst)
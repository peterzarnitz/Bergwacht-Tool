# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Grundausbildung

# Create your views here.

@login_required
def index(request):
    grundausbildungen = Grundausbildung.objects.all()
    return render(request, 'ausbildung/ausbildung_menu.html', {grundausbildungen: 'grundausbildungen'})

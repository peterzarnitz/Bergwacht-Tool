# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader

from .models import Dienst


def index(request):
    dienst_list = Dienst.objects.order_by('dienstbeginn')
    template = loader.get_template('dienstplan/index.html')
    context = {
        'dienst_list': dienst_list,
    }
    return HttpResponse(template.render(context, request))

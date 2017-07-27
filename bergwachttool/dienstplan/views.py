# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Dienst


def index(request):
    dienst_list = Dienst.objects.order_by('dienstbeginn')
    template = loader.get_template('dienstplan/index.html')
    context = {
        'dienst_list': dienst_list,
    }
    return HttpResponse(template.render(context, request))


def dienst_detail(request, dienstnummer):
    try:
        dienst = Dienst.objects.get(dienstnummer=dienstnummer)
    except Dienst.DoesNotExist:
        raise Http404("Dienst existiert nicht")
    return render(request, 'dienstplan/dienst_detail.html', {'dienst': dienst})

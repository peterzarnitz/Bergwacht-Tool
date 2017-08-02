# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Dienst, Mitglied


def index(request):
    return render(request, 'dienstplan/index.html')


def dienst_list(request):
    dienst_list = Dienst.objects.order_by('dienstbeginn')
    template = loader.get_template('dienstplan/dienst_list.html')
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


def mitglieder_overview(request):
    mitglieder_list = Mitglied.objects.filter(user__is_superuser='False').order_by('user__last_name')  #
    mitglieder_list.filter()
    template = loader.get_template('dienstplan/mitglieder_list.html')
    context = {
        'mitglieder_list': mitglieder_list,
    }
    return HttpResponse(template.render(context, request))

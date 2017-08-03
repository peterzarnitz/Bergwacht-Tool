# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import DienstTeilnahmeForm
from .models import Dienst, Mitglied


@login_required
def index(request):
    return render(request, 'dienstplan/index.html')


@login_required
def dienst_list(request):
    dienst_list = Dienst.objects.order_by('dienstbeginn')
    template = loader.get_template('dienstplan/dienst_list.html')
    context = {
        'dienst_list': dienst_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def dienst_detail(request, dienstnummer):
    try:
        dienst = Dienst.objects.get(dienstnummer=dienstnummer)
    except Dienst.DoesNotExist:
        raise Http404("Dienst existiert nicht")
    return render(request, 'dienstplan/dienst_detail.html', {'dienst': dienst})


@login_required
def dienst_anmeldung(request, dienstnummer):
    try:
        dienst = Dienst.objects.get(dienstnummer=dienstnummer)
    except Dienst.DoesNotExist:
        raise Http404("Dienst existiert nicht")

    if request.method == "POST":
        form = DienstTeilnahmeForm(request.POST)
        if form.is_valid():
            anmeldung = form.save(commit=False)
            anmeldung.mitglied = Mitglied.objects.get(user=request.user)
            anmeldung.dienstnummer = dienst
            anmeldung.save()
            return redirect('dienst_detail', dienstnummer=dienstnummer)
    else:
        form = DienstTeilnahmeForm()
    return render(request, 'dienstplan/dienst_anmeldung.html', {'form': form, 'dienst': dienst})


@login_required
def mitglieder_overview(request):
    mitglieder_list = Mitglied.objects.filter(user__is_superuser='False').order_by('user__last_name')  #
    mitglieder_list.filter()
    template = loader.get_template('dienstplan/mitglieder_list.html')
    context = {
        'mitglieder_list': mitglieder_list,
    }
    return HttpResponse(template.render(context, request))

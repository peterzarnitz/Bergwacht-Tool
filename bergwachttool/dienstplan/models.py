# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Nutzer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nachname = models.CharField(max_length=50, verbose_name='Nachname', null=True, blank=True)
    vorname = models.CharField(max_length=50, verbose_name='Vorname', null=True, blank=True)
    handy = models.CharField(max_length=20, verbose_name='Handynummer', null=True, blank=True)
    adresse_strasse = models.CharField(max_length=100, verbose_name='Straße & Hnr.', null=True, blank=True)
    adresse_plz = models.CharField(max_length=6, verbose_name='PLZ', null=True, blank=True)
    adresse_ort = models.CharField(max_length=100, verbose_name='Stadt', null=True, blank=True)
    geb_datum = models.DateField(verbose_name='Geburtsdatum', null=True, blank=True)
    bw_eintritt = models.DateField(verbose_name='Bergwacht-Eintritt', null=True, blank=True)


class Dienstgebiet(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')


class Dienstart(models.Model):
    name = models.CharField(max_length=40, verbose_name='Dienstart')


class Dienst(models.Model):
    id = models.UUIDField(primary_key=True, verbose_name='Dienstnummer')
    dienstgebiet = models.ForeignKey(Dienstgebiet, on_delete=models.CASCADE)
    dienstbeginn = models.DateTimeField(verbose_name='Dienstbeginn')
    dienstende = models.DateTimeField(verbose_name='Dienstende')
    art = models.ForeignKey(Dienstart, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_nutzer(sender, instance, created, **kwargs):
    if created:
        Nutzer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_nutzer(sender, instance, **kwargs):
    instance.userprofile.save()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Nutzer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    handy = models.CharField(max_length=20, verbose_name='Handynummer', null=True, blank=True)
    adresse_strasse = models.CharField(max_length=100, verbose_name='Straße & Hnr.', null=True, blank=True)
    adresse_plz = models.CharField(max_length=6, verbose_name='PLZ', null=True, blank=True)
    adresse_ort = models.CharField(max_length=100, verbose_name='Stadt', null=True, blank=True)
    geb_datum = models.DateField(verbose_name='Geburtsdatum', null=True, blank=True)
    bw_eintritt = models.DateField(verbose_name='Bergwacht-Eintritt', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Nutzer'

    def __str__(self):
        return self.user.username


class Dienstgebiet(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Dienstgebiete'

    def __str__(self):
        return self.name


class Dienstart(models.Model):
    name = models.CharField(max_length=40, verbose_name='Dienstart')

    class Meta:
        verbose_name_plural = 'Dienstarten'

    def __str__(self):
        return self.name


class Dienst(models.Model):
    dienstnummer = models.AutoField(primary_key=True, verbose_name='Dienstnummer')
    dienstgebiet = models.ForeignKey(Dienstgebiet, on_delete=models.CASCADE)
    dienstbeginn = models.DateTimeField(verbose_name='Dienstbeginn')
    dienstende = models.DateTimeField(verbose_name='Dienstende')
    art = models.ForeignKey(Dienstart, on_delete=models.CASCADE)
    bemerkung = models.TextField(max_length=500, verbose_name='Bemerkungen', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Dienste'

    def __str__(self):
        return str(self.dienstnummer)


@receiver(post_save, sender=User)
def create_nutzer(sender, instance, created, **kwargs):
    if created:
        Nutzer.objects.create(user=instance)
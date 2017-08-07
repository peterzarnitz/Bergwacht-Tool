# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Grundausbildung(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    anwaerterfahrt_sommer = models.BooleanField(verbose_name='Anwaerterfahrt Sommer')
    anwaerterfahrt_winter = models.BooleanField(verbose_name='Anwaerterfahrt Winter')

    grundausbildung_winter = models.BooleanField(verbose_name='Grundausbildung Winter')
    winterrettung = models.BooleanField(verbose_name='Winterrettung')
    behelfs_bergrettung = models.BooleanField(verbose_name='Behelfsmaessige Bergrettung')
    planmae_bergrettung = models.BooleanField(verbose_name='Planmaessige Bergrettung')

    funk = models.BooleanField(verbose_name='Funk')
    akia = models.BooleanField(verbose_name='Akia')
    orientierung = models.BooleanField(verbose_name='Orientierung und Kartenkunde')

    natschutz_exkursion = models.BooleanField(verbose_name='Anwaerterfahrt Sommer')

    eignungstest_sommer = models.BooleanField(verbose_name='Eignungstest Sommer')
    eignungstest_winter = models.BooleanField(verbose_name='Eignungstest Winter')
    pruefung_winter = models.BooleanField(verbose_name='Prüfung Winter')
    pruefung_sommer = models.BooleanField(verbose_name='Prüfung Sommer')
    pruefung_natschutz = models.BooleanField(verbose_name='Prüfung Naturschutz')

    class Meta:
        verbose_name_plural = 'Grundausbildung'

    def __str__(self):
        return self.user.username

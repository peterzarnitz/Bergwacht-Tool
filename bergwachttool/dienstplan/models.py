# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS_CHOICES = (
    ('AEK', 'Aktive Einsatzkraft'),
    ('ANW', 'Anwaerter'),
    ('NEK', 'Nicht-aktive Einsatzkraft'),
)
FUNKTION_CHOICES = (
    ('FAR', 'Fahrer'),
    ('DVL', 'Dienstverantwortlicher'),
)


class Mitglied(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    handy = models.CharField(max_length=20, verbose_name='Handynummer', null=True, blank=True)
    adresse_strasse = models.CharField(max_length=100, verbose_name='Straße & Hnr.', null=True, blank=True)
    adresse_plz = models.CharField(max_length=6, verbose_name='PLZ', null=True, blank=True)
    adresse_ort = models.CharField(max_length=100, verbose_name='Stadt', null=True, blank=True)
    geb_datum = models.DateField(verbose_name='Geburtsdatum', null=True, blank=True)
    bw_eintritt = models.DateField(verbose_name='Bergwacht-Eintritt', null=True, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='Anwaerter')

    class Meta:
        verbose_name_plural = 'Mitglieder'
        ordering = ['status', 'user__last_name']

    def __str__(self):
        return self.user.username

    def getAnwaerter(self):
        return Mitglied.objects.filter(status='ANW')

    def getAEK(self):
        return Mitglied.objects.filter(status='AEK')

    def getAlter(self):
        return 0  # TODO: datetime.date.today() - self.geb_datum

    def getDiensteAngemeldet(self):
        return nimmtTeilanDienst.objects.filter(mitglied=self).count()




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


class Fahrzeug(models.Model):
    kennzeichen = models.CharField(max_length=10, verbose_name='Kennzeichen')
    bezeichnung = models.CharField(max_length=10, verbose_name='Bezeichnung')
    typ = models.CharField(max_length=50, verbose_name='Typ')
    standort = models.CharField(max_length=50, verbose_name='Standort')
    naechsteHU = models.DateField(verbose_name='Naechste HU faellig am')

    class Meta:
        verbose_name_plural = 'Fahrzeuge'

    def __str__(self):
        return self.bezeichnung


class Dienst(models.Model):
    dienstnummer = models.AutoField(primary_key=True, verbose_name='Dienstnummer')
    dienstgebiet = models.ForeignKey(Dienstgebiet, on_delete=models.CASCADE)
    dienstbeginn = models.DateTimeField(verbose_name='Dienstbeginn')
    dienstende = models.DateTimeField(verbose_name='Dienstende')
    art = models.ForeignKey(Dienstart, on_delete=models.CASCADE)
    bemerkung = models.TextField(max_length=500, verbose_name='Bemerkungen', blank=True, null=True)
    mitglieder = models.ManyToManyField(Mitglied, through='nimmtTeilanDienst',
                                        through_fields=('dienstnummer', 'mitglied'), )
    fahrzeug = models.ForeignKey(Fahrzeug, on_delete=models.CASCADE, null=True, blank=True)
    minaek = models.IntegerField(verbose_name='Geforderte AEK', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Dienste'

    def getAEKcount(self):
        return self.mitglieder.filter(status='AEK').count()

    def __str__(self):
        return str(self.dienstnummer)


class nimmtTeilanDienst(models.Model):
    dienstnummer = models.ForeignKey(Dienst, on_delete=models.CASCADE)
    mitglied = models.ForeignKey(Mitglied, on_delete=models.CASCADE)
    von = models.DateTimeField(verbose_name='Von')
    bis = models.DateTimeField(verbose_name='Bis')
    funktion = models.CharField(max_length=3, null=True, blank=True, choices=FUNKTION_CHOICES)
    kommentar = models.TextField(verbose_name='Kommentar', max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Dienstteilnahme'

    def __str__(self):
        return str(self.dienstnummer) + ' - ' + self.mitglied.user.last_name + '.' + self.mitglied.user.first_name


@receiver(post_save, sender=User)
def create_nutzer(sender, instance, created, **kwargs):
    if created:
        Mitglied.objects.create(user=instance)

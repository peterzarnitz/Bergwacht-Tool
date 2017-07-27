# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-27 12:10
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dienst',
            fields=[
                ('dienstnummer', models.AutoField(primary_key=True, serialize=False, verbose_name='Dienstnummer')),
                ('dienstbeginn', models.DateTimeField(verbose_name='Dienstbeginn')),
                ('dienstende', models.DateTimeField(verbose_name='Dienstende')),
                ('bemerkung', models.TextField(blank=True, max_length=500, null=True, verbose_name='Bemerkungen')),
            ],
            options={
                'verbose_name_plural': 'Dienste',
            },
        ),
        migrations.CreateModel(
            name='Dienstart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Dienstart')),
            ],
            options={
                'verbose_name_plural': 'Dienstarten',
            },
        ),
        migrations.CreateModel(
            name='Dienstgebiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Dienstgebiete',
            },
        ),
        migrations.CreateModel(
            name='Mitglied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handy', models.CharField(blank=True, max_length=20, null=True, verbose_name='Handynummer')),
                ('adresse_strasse',
                 models.CharField(blank=True, max_length=100, null=True, verbose_name='Stra\xdfe & Hnr.')),
                ('adresse_plz', models.CharField(blank=True, max_length=6, null=True, verbose_name='PLZ')),
                ('adresse_ort', models.CharField(blank=True, max_length=100, null=True, verbose_name='Stadt')),
                ('geb_datum', models.DateField(blank=True, null=True, verbose_name='Geburtsdatum')),
                ('bw_eintritt', models.DateField(blank=True, null=True, verbose_name='Bergwacht-Eintritt')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Mitglieder',
            },
        ),
        migrations.CreateModel(
            name='nimmtTeilanDienst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('von', models.DateTimeField(verbose_name='Von')),
                ('bis', models.DateTimeField(verbose_name='Bis')),
                ('kommentar', models.TextField(max_length=200, verbose_name='Kommentar')),
                (
                    'dienstnummer',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dienstplan.Dienst')),
                ('mitglied', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dienstplan.Mitglied')),
            ],
        ),
        migrations.AddField(
            model_name='dienst',
            name='art',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dienstplan.Dienstart'),
        ),
        migrations.AddField(
            model_name='dienst',
            name='dienstgebiet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dienstplan.Dienstgebiet'),
        ),
        migrations.AddField(
            model_name='dienst',
            name='mitglieder',
            field=models.ManyToManyField(through='dienstplan.nimmtTeilanDienst', to='dienstplan.Mitglied'),
        ),
    ]

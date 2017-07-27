# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-27 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dienstplan', '0003_auto_20170726_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dienst',
            options={'verbose_name_plural': 'Dienste'},
        ),
        migrations.AlterModelOptions(
            name='dienstart',
            options={'verbose_name_plural': 'Dienstarten'},
        ),
        migrations.AlterModelOptions(
            name='dienstgebiet',
            options={'verbose_name_plural': 'Dienstgebiete'},
        ),
        migrations.AlterModelOptions(
            name='nutzer',
            options={'verbose_name_plural': 'Nutzer'},
        ),
        migrations.RemoveField(
            model_name='dienst',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nutzer',
            name='nachname',
        ),
        migrations.RemoveField(
            model_name='nutzer',
            name='vorname',
        ),
        migrations.AddField(
            model_name='dienst',
            name='dienstnummer',
            field=models.AutoField(default=0, primary_key=True, serialize=False, verbose_name='Dienstnummer'),
            preserve_default=False,
        ),
    ]

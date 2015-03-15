# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0021_patient_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='lastName',
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(verbose_name='Адрес'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthDate',
            field=models.DateField(verbose_name='Дата Рождения'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='organization',
            field=models.TextField(verbose_name='Место работы'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='patronymic',
            field=models.TextField(verbose_name='Отчество'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='position',
            field=models.TextField(verbose_name='Должность'),
            preserve_default=True,
        ),
    ]

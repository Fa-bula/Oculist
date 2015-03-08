# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='is_working',
        ),
        migrations.AddField(
            model_name='doctor',
            name='birthDate',
            field=models.DateField(verbose_name='Дата рождения', default=datetime.datetime(2015, 3, 1, 21, 21, 24, 395273, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='education',
            field=models.TextField(verbose_name='Образование'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='firstName',
            field=models.TextField(verbose_name='Имя'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='lastName',
            field=models.TextField(verbose_name='Фамилия'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='patronymic',
            field=models.TextField(verbose_name='Отчество'),
            preserve_default=True,
        ),
    ]

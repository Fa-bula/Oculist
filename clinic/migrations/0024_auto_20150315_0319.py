# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0023_auto_20150315_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='firstName',
            field=models.TextField(default='Булат', verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='lastName',
            field=models.TextField(default='Фатыхов', verbose_name='Фамилия'),
            preserve_default=False,
        ),
    ]

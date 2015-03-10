# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0017_service_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doctor_type',
            field=models.IntegerField(default=1, choices=[(1, 'Кардиолог'), (2, 'Терапевт')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.IntegerField(default=1, choices=[(1, 'Прием у врача'), (2, 'Массаж')]),
            preserve_default=False,
        ),
    ]

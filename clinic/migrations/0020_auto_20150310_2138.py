# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0019_remove_service_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_type',
            new_name='serviceType',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_type',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctorType',
            field=models.IntegerField(choices=[(1, 'Кардиолог'), (2, 'Терапевт')], default=1, verbose_name='Специализация'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0014_schedule_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='weekdayFrom',
            field=models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятнича'), (6, 'Суббота'), (7, 'Воскресенье')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='weekdayTo',
            field=models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятнича'), (6, 'Суббота'), (7, 'Воскресенье')]),
            preserve_default=True,
        ),
    ]

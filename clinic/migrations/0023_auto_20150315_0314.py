# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0022_auto_20150315_0309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='date',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='hourFrom',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='hourTo',
        ),
        migrations.AddField(
            model_name='visit',
            name='dateTime',
            field=models.DateTimeField(default="2015-01-01 00:00"),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0013_auto_20150308_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='name',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]

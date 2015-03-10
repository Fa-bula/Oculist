# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0016_auto_20150310_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='doctor',
            field=models.ForeignKey(to='clinic.Doctor', default=1),
            preserve_default=False,
        ),
    ]

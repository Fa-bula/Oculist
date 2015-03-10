# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0018_auto_20150310_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='name',
        ),
    ]

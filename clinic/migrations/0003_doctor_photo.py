# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_auto_20150302_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.FilePathField(verbose_name='/home/bulat/projects/Okulist/clinic/static/clinic', default='/home/bulat/projects/Okulist/clinic/static/clinic/'),
            preserve_default=False,
        ),
    ]

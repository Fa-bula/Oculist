# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_auto_20150308_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.FilePathField(path='/home/bulat/projects/Okulist/clinic/static/clinic/img/'),
            preserve_default=True,
        ),
    ]

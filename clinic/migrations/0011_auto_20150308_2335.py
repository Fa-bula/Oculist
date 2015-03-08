# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0010_auto_20150308_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.FilePathField(path='/home/bulat/projects/Okulist/clinic/static/clinic/img/doctors/'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_doctor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.FilePathField(path='/home/bulat/projects/Okulist/clinic/static/clinic'),
            preserve_default=True,
        ),
    ]

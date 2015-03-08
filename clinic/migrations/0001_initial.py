# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('pubDate', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('patronymic', models.TextField()),
                ('education', models.TextField()),
                ('birth_date', models.DateField()),
                ('is_working', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
                ('hourFrom', models.TimeField()),
                ('hourTo', models.TimeField()),
                ('doctor', models.ForeignKey(to='clinic.Doctor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('patronymic', models.TextField()),
                ('birthDate', models.DateField()),
                ('address', models.TextField()),
                ('organization', models.TextField()),
                ('position', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('weekdayFrom', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wensday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('weekdayTo', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wensday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('hourFrom', models.TimeField()),
                ('hourTo', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('cost', models.IntegerField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('hourFrom', models.TimeField()),
                ('hourTo', models.TimeField()),
                ('patient', models.ForeignKey(to='clinic.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='doctor',
            name='schedule',
            field=models.ForeignKey(to='clinic.Schedule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='service',
            field=models.ForeignKey(to='clinic.Service'),
            preserve_default=True,
        ),
    ]

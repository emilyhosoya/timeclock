# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0008_auto_20141104_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_active',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_created',
        ),
        migrations.AlterField(
            model_name='job',
            name='job_name',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Name', blank=True),
            preserve_default=True,
        ),
    ]

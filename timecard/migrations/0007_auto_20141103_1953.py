# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0006_auto_20141103_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_active',
            field=models.BooleanField(default=True, verbose_name=b'Active'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_created',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_active',
            field=models.BooleanField(default=True, verbose_name=b'Active'),
            preserve_default=True,
        ),
    ]

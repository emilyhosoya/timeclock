# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0005_auto_20141103_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_added',
        ),
        migrations.AddField(
            model_name='job',
            name='job_created',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]

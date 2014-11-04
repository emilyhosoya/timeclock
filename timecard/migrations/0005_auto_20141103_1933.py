# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0004_job_job_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_added',
            field=models.DateField(default=datetime.date.today, editable=False),
            preserve_default=True,
        ),
    ]

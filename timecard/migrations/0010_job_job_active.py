# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0009_auto_20141104_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_active',
            field=models.BooleanField(default=True, verbose_name=b'Active'),
            preserve_default=True,
        ),
    ]

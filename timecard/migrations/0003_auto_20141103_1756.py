# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0002_auto_20141103_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

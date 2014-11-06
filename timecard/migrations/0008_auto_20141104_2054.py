# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0007_auto_20141103_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ('job_order',)},
        ),
        migrations.AddField(
            model_name='job',
            name='job_order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='job_name',
            field=models.CharField(max_length=60, verbose_name=b'Name'),
            preserve_default=True,
        ),
    ]

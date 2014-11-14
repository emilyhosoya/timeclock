# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0015_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='user',
            field=models.ForeignKey(to='timecard.UserProfile'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0010_job_job_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_active',
            new_name='isActive',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_active',
            new_name='isActive',
        ),
    ]

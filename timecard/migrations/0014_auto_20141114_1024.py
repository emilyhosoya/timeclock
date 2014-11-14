# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timecard', '0013_remove_employee_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='UserProfile',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='isActive',
            new_name='is_active',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ella_attachments', '0002_auto_20150506_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created', editable=False),
        ),
    ]

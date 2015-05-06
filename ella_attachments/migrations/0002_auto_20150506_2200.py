# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ella_attachments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='publishables',
            field=models.ManyToManyField(to='core.Publishable', verbose_name='Publishables', blank=True),
        ),
    ]

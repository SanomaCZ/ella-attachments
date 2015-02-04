# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ella_attachments.models
import ella.core.cache.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150106_1411'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug')),
                ('description', models.TextField(default=None, null=True, verbose_name='Description', blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created', editable=False)),
                ('attachment', models.FileField(upload_to=ella_attachments.models.upload_to, verbose_name='Attachment')),
                ('photo', ella.core.cache.fields.CachedForeignKey(related_name='photos', verbose_name='Photo', blank=True, to='photos.Photo', null=True)),
                ('publishables', models.ManyToManyField(to='core.Publishable', null=True, verbose_name='Publishables', blank=True)),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Attachment',
                'verbose_name_plural': 'Attachments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
                ('mimetype', models.CharField(help_text='consult http://www.sfsu.edu/training/mimetype.htm', max_length=100, verbose_name='Mime type')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attachment',
            name='type',
            field=ella.core.cache.fields.CachedForeignKey(default=None, blank=True, to='ella_attachments.Type', null=True, verbose_name='Attachment type'),
            preserve_default=True,
        ),
    ]

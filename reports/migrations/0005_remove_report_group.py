# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 04:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_report_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='group',
        ),
    ]

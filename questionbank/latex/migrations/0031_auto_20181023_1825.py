# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0030_auto_20181023_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='block',
            field=models.IntegerField(blank=True),
        ),
    ]

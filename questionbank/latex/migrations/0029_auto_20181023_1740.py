# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0028_auto_20181023_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]

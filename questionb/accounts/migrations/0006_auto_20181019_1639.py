# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-19 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181019_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subject',
            field=models.CharField(choices=[('1', 'Subject-1'), ('2', 'Subject-2'), ('3', 'Subject-3'), ('4', 'Subject-4')], max_length=20, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-19 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('latex', '0013_subject_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='user',
        ),
    ]

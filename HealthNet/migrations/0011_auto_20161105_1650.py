# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-05 20:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0010_auto_20161105_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 5, 17, 20, 58, 883798)),
        ),
    ]

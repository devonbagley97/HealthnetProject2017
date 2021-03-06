# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-20 18:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HealthNet', '0018_auto_20161108_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='E_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='E_contactUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='patient',
            name='E_contact_address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='E_contact_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='E_contact_phoneNum',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 20, 14, 17, 27, 217842)),
        ),
    ]

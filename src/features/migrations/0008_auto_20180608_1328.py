# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_feature_default_enabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurestate',
            name='type',
        ),
        migrations.AddField(
            model_name='feature',
            name='type',
            field=models.CharField(choices=[('FLAG', 'Feature Flag'), ('CONFIG', 'Remote Config')], default='FLAG', max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 14:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypt', '0009_auto_20160708_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptrecdata',
            name='mobileno',
            field=models.CharField(default='+91', max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\*?1?\\d{9,15}$')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 13:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0004_auto_20160708_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createrecdata',
            name='mobileno',
            field=models.CharField(default='+91', max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 14:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypt', '0014_auto_20160708_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptrecdata',
            name='rollno',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator(message="Roll number must be entered in the format: '15XX101'.", regex='^(\\d{2}|\\d{8})([a-z]{2}|[A-Z]{2})\\d{2,3}([a-z]{1}|[A-Z]{1})?$')]),
        ),
    ]

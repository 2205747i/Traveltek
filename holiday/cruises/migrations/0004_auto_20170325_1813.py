# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruises', '0003_auto_20170325_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='cruise',
            name='adults',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='cruise',
            name='children',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
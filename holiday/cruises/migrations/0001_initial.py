# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabin_number', models.CharField(blank=True, max_length=128)),
                ('deck_code', models.CharField(blank=True, max_length=128)),
                ('deck_name', models.CharField(blank=True, max_length=128)),
                ('x1', models.IntegerField(blank=True)),
                ('x2', models.IntegerField(blank=True)),
                ('y1', models.IntegerField(blank=True)),
                ('y2', models.IntegerField(blank=True)),
                ('image', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CabinGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default=None, max_length=128)),
                ('grade_number', models.CharField(default=None, max_length=128)),
                ('result_number', models.CharField(default=None, max_length=128)),
                ('title', models.CharField(default=None, max_length=128)),
                ('session_key', models.CharField(default=None, max_length=128)),
                ('cabin_code', models.CharField(default=None, max_length=128)),
                ('farename', models.CharField(default=None, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('adults', models.IntegerField(blank=True, default=2)),
                ('children', models.IntegerField(blank=True, default=0)),
                ('sail_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('nights', models.IntegerField(blank=True, default=None, null=True)),
                ('sail_nights', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('code_to_cruise_id', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('slug', models.URLField(blank=True, unique=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceDetection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='faceRectangle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.IntegerField()),
                ('top', models.IntegerField()),
                ('left', models.IntegerField()),
                ('width', models.IntegerField()),
                ('heigth', models.IntegerField()),
            ],
        ),
    ]

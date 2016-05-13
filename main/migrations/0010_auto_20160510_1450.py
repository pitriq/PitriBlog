# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(match='/.+(\\.png$|\\.jpeg$|\\.jpg$)/', path='/home/images'),
        ),
    ]

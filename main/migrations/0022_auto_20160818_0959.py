# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-18 12:59
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20160512_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/pitri/Documentos/django-projects/myBlog/media/articles-img/'), upload_to=b''),
        ),
    ]
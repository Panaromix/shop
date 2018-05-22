# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-18 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171018_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='description_ukr',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='keyword_ukr',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='title_ukr',
            field=models.CharField(max_length=320, null=True),
        ),
    ]
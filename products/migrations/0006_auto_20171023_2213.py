# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image_image_mini'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description_collection_mini',
            field=models.CharField(blank=True, default=None, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='description_collection_mini_ukr',
            field=models.CharField(blank=True, default=None, max_length=140, null=True),
        ),
    ]

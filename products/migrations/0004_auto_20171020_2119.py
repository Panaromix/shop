# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20171018_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='description_ukr',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='keyword_ukr',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='title_ukr',
        ),
    ]

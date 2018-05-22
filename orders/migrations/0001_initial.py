# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0010_auto_20171108_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call_Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_me_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('call_me_phone', models.CharField(blank=True, default=None, max_length=64, null=True)),
            ],
            options={
                'verbose_name': 'Перезвоните мне',
                'verbose_name_plural': 'Перезвоните мне',
            },
        ),
        migrations.CreateModel(
            name='Find_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=48, null=True)),
                ('customer_address', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('session_key', models.CharField(default=None, max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.FileField(upload_to='projects/')),
            ],
            options={
                'verbose_name': 'Спецификация на просчет',
                'verbose_name_plural': 'Спецификации на просчет',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('customer_email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('customer_phone', models.CharField(blank=True, default=None, max_length=48, null=True)),
                ('customer_address', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('comments', models.TextField(blank=True, default=None, null=True)),
                ('session_key', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ордер на покупкуr',
                'verbose_name_plural': 'Ордеры на покупку',
            },
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('nmb', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('nmb', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'verbose_name': 'Товар в ордере',
                'verbose_name_plural': 'Товары в ордере',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(blank=True, default=None, max_length=48, null=True)),
            ],
            options={
                'verbose_name': 'Статус ордера',
                'verbose_name_plural': 'Статусы ордера',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
        migrations.AddField(
            model_name='find_project',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
    ]
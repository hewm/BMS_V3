# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('books_es', models.ManyToManyField(to='APP01.Books')),
            ],
        ),
    ]

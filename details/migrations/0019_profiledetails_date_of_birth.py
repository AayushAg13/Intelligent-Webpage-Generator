# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0018_publicationdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='date_of_birth',
            field=models.DateField(default='1998-10-10'),
            preserve_default=False,
        ),
    ]

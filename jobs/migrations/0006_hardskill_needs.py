# Generated by Django 3.0.6 on 2020-05-28 13:00

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200528_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardskill',
            name='needs',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=1),
            preserve_default=False,
        ),
    ]

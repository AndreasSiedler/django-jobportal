# Generated by Django 3.0.6 on 2020-05-22 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_profile_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tasks',
            field=models.ManyToManyField(to='jobs.Task'),
        ),
    ]

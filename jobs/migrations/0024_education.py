# Generated by Django 3.0.6 on 2020-06-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0023_job_offers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
    ]

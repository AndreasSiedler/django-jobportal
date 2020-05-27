# Generated by Django 3.0.6 on 2020-05-27 20:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0002_auto_20200526_1349'),
        ('profiles', '0002_auto_20200526_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterUniqueTogether(
            name='candidate',
            unique_together={('user', 'jobtype')},
        ),
        migrations.AlterIndexTogether(
            name='candidate',
            index_together={('user', 'jobtype')},
        ),
    ]

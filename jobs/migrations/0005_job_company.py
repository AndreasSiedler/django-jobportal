# Generated by Django 3.0.6 on 2020-05-23 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_remove_candidate_avatar'),
        ('jobs', '0004_auto_20200523_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Company'),
        ),
    ]

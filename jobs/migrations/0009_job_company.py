# Generated by Django 3.0.5 on 2020-04-16 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200416_0936'),
        ('jobs', '0008_auto_20200415_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Company'),
        ),
    ]

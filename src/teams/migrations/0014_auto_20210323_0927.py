# Generated by Django 3.1.7 on 2021-03-23 13:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0013_auto_20210323_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='users',
        ),
        migrations.AddField(
            model_name='team',
            name='users',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None),
        ),
    ]

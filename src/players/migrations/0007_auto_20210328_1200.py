# Generated by Django 3.1.7 on 2021-03-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_auto_20210328_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goalie',
            name='teamAbbreviation',
        ),
        migrations.AddField(
            model_name='goalie',
            name='teamId',
            field=models.IntegerField(default=0),
        ),
    ]

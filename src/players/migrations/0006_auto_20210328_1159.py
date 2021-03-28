# Generated by Django 3.1.7 on 2021-03-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_goalie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='teamAbbreviation',
        ),
        migrations.AddField(
            model_name='player',
            name='teamId',
            field=models.IntegerField(default=0),
        ),
    ]

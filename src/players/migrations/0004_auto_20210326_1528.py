# Generated by Django 3.1.7 on 2021-03-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20210325_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='firstName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='lastName',
        ),
        migrations.AddField(
            model_name='player',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]

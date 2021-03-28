# Generated by Django 3.1.7 on 2021-03-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='firstName',
        ),
        migrations.AddField(
            model_name='player',
            name='lastName',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
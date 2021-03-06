# Generated by Django 3.1.7 on 2021-04-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0020_auto_20210405_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='faceOffWinPercentage',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='penaltyKillPercentage',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='powerPlayGoals',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='powerPlayGoalsAgainst',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='powerPlayPercentage',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='savePctg',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='shotsAllowed',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='shotsPerGame',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
    ]

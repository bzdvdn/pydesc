# Generated by Django 2.0.7 on 2018-08-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Закрыта:'),
        ),
        migrations.AlterField(
            model_name='task',
            name='closetime',
            field=models.DateField(verbose_name='Закрыта в:'),
        ),
    ]

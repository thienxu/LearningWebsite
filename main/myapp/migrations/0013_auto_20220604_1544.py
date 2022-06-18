# Generated by Django 2.2 on 2022-06-04 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20220601_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='history',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 15, 44, 43, 151273)),
        ),
        migrations.AlterField(
            model_name='problem',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 15, 44, 43, 151273)),
        ),
    ]
# Generated by Django 2.2 on 2022-06-18 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20220604_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='problem_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='history',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 19, 55, 32, 322500)),
        ),
        migrations.AlterField(
            model_name='problem',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 19, 55, 32, 322500)),
        ),
    ]

# Generated by Django 3.1.7 on 2021-11-13 05:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_auto_20211113_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commets_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 5, 35, 49, 850181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 5, 35, 49, 849192, tzinfo=utc)),
        ),
    ]

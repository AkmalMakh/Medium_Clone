# Generated by Django 3.1.7 on 2021-11-13 05:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_auto_20211113_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commets_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 5, 37, 15, 978472, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 5, 37, 15, 977890, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-02 05:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211002_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commets_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 2, 5, 7, 38, 454669, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 2, 5, 7, 38, 454669, tzinfo=utc)),
        ),
    ]

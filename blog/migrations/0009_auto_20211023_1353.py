# Generated by Django 3.2.6 on 2021-10-23 04:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20211023_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 4, 53, 30, 333331, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 4, 53, 30, 333331, tzinfo=utc)),
        ),
    ]

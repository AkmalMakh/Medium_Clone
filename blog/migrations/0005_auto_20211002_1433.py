# Generated by Django 3.2.6 on 2021-10-02 05:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211002_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentContent',
            field=models.TextField(default='write something'),
        ),
        migrations.AddField(
            model_name='post',
            name='postContent',
            field=models.TextField(default='write something'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 2, 5, 33, 6, 312280, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 2, 5, 33, 6, 312280, tzinfo=utc)),
        ),
    ]
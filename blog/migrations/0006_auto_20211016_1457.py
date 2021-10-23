# Generated by Django 3.2.6 on 2021-10-16 05:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211002_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentContent',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='postContent',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 16, 5, 56, 8, 965542, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 16, 5, 56, 8, 964543, tzinfo=utc)),
        ),
    ]
# Generated by Django 2.1.7 on 2019-03-27 19:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20190327_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 27, 19, 25, 59, 194360, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='group',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 27, 19, 25, 59, 178359, tzinfo=utc)),
        ),
    ]

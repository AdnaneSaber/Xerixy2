# Generated by Django 3.1.7 on 2021-05-09 06:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 9, 6, 35, 58, 991639, tzinfo=utc)),
        ),
    ]

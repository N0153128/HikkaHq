# Generated by Django 2.2.5 on 2019-10-14 23:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HikkaHq', '0005_auto_20191015_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date_c',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 23, 54, 59, 285341, tzinfo=utc), verbose_name='Date published'),
        ),
    ]
# Generated by Django 2.2.5 on 2019-10-15 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikkaHq', '0013_auto_20191015_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(blank=True, default='', null=True, verbose_name='Date published'),
        ),
    ]
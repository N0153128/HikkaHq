# Generated by Django 2.2.5 on 2019-10-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HikkaHq', '0007_auto_20191015_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date_c',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date published'),
        ),
    ]
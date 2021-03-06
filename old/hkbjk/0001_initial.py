# Generated by Django 2.2.5 on 2019-10-14 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_title', models.CharField(max_length=100)),
                ('thread_text', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('category', models.CharField(max_length=50)),
                ('thread_author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=2500)),
                ('comment_author', models.CharField(max_length=200)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HikkaHq.Thread')),
            ],
        ),
    ]

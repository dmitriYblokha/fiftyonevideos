# Generated by Django 4.0.6 on 2022-08-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]

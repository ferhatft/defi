# Generated by Django 3.1.7 on 2021-04-29 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0004_auto_20210428_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='anahaber',
            field=models.BooleanField(default=False, verbose_name='ana haber'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='sliderhaber',
            field=models.BooleanField(default=False, verbose_name='slider ekle'),
        ),
    ]

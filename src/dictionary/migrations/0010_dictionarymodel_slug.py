# Generated by Django 3.1.7 on 2021-03-27 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0009_auto_20210328_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionarymodel',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='uzantı'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_auto_20210320_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionarymodel',
            name='title',
            field=models.CharField(blank=True, max_length=500, unique=True, verbose_name='Ana Başlık '),
        ),
    ]

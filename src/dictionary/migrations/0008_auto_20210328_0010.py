# Generated by Django 3.1.7 on 2021-03-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0007_auto_20210327_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionarymodel',
            name='title',
            field=models.SlugField(blank=True, max_length=500, unique=True, verbose_name='Ana Başlık '),
        ),
    ]

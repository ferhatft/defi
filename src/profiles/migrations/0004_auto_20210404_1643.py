# Generated by Django 3.1.7 on 2021-04-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210319_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='abaout',
            field=models.TextField(max_length=500, verbose_name='Hakkında'),
        ),
    ]